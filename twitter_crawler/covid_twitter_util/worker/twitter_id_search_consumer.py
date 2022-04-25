import threading
from queue import Empty

import tweepy
from loguru import logger

from common_util.config_handler import ConfigHandler
from db_util import db_helper
from twitter_util import twitter_preprocess_helper, keyword_helper
from twitter_util.twitter_preprocess_helper import is_tweet_english

MELBOURNE_PLACE_ID = '01864a8a64df9dc4'

NUM_TWEETS_PER_REQUEST = 50


class TwitterIdSearchConsumer(threading.Thread):
    """
    producer: read tweet id into a queue
    """

    def __init__(self, queue, end_signal_helper):
        threading.Thread.__init__(self)

        self.__queue = queue
        self.__end_signal_helper = end_signal_helper

        self.__config = ConfigHandler()
        self.__id_list = []

        self.__db_helper = db_helper.DbHelper()

        # api authentication
        self.__tweepy_client = tweepy.Client(
            bearer_token=self.__config.get_api_token(),
            wait_on_rate_limit=True
        )

    def __push_id_to_search(self, tweet_id):
        """
        queue size is NUM_TWEETS_PER_REQUEST, if the queue size reaches NUM_TWEETS_PER_REQUEST, query NUM_TWEETS_PER_REQUEST
         ids with API, then clear queue for next NUM_TWEETS_PER_REQUEST.

        This logic is created because of Twitter API's 100 ID query limitation
        :param tweet_id:
        :return: null

        author: xiaotian li
        """

        if len(self.__id_list) >= NUM_TWEETS_PER_REQUEST:
            # query NUM_TWEETS_PER_REQUEST ids each time
            # it is better to use tweets mentioned melbourne, rather than located in melbourne
            # because tweets located in melbourne can discuss covid on the other place, and number
            # of tweets are too low
            # self.__query_ids_located_in_melbourne(self.__id_list)
            self.__query_ids_mentioned_melbourne(self.__id_list)
            # free the queue
            del self.__id_list
            self.__id_list = []
        else:
            self.__id_list.append(str(tweet_id))

    def __query_ids_mentioned_melbourne(self, id_list):
        """
        fetch tweets that mentioned melbourne, or place id is melbourne
        """

        if len(id_list) > 0:
            response = self.__tweepy_client.get_tweets(
                ids=id_list,
                expansions='geo.place_id',
                tweet_fields='id,text,lang,source,created_at,geo',
                user_fields=None,
                place_fields='country,country_code,geo,name'
            )

            # logger.debug('handling a response tweet patch')

            if response.data is None:
                logger.warning('get an Empty response from query ids')
                return

            raw_twitters = response.data
            # find all melbourne raw_twitters
            for raw_twitter in raw_twitters:
                # melbourne condition for each tweet
                # language filter
                if self.__config.is_fetch_english_tweet_only() and not is_tweet_english(raw_twitter):
                    continue

                full_text = twitter_preprocess_helper.get_full_text(raw_twitter)

                # melbourne keyword filter
                is_tweet_mentioned_melb = keyword_helper.is_text_contains_a_keyword(
                    keyword='melbourne',
                    input_text=full_text
                )

                is_tweet_from_melbourne = raw_twitter.get('geo') is not None \
                                          and raw_twitter.get('geo').get('place_id') == MELBOURNE_PLACE_ID

                if not (is_tweet_mentioned_melb or is_tweet_from_melbourne):
                    continue

                # if mentioned melb or located in melb
                logger.debug('Mentioned or located melbourne, full text: ' + full_text)

                # other keyword filter
                if not keyword_helper.is_text_match_keywords(full_text):
                    continue

                logger.debug('passed keyword filter')
                tweet_dict_for_storage = twitter_preprocess_helper.preprocess_twitter(raw_twitter)

                # put it to db
                self.__db_helper.put_twitter_to_db(tweet_dict_for_storage)

    @DeprecationWarning
    def __query_ids_located_in_melbourne(self, id_list):
        """
        fetch tweets that located melbourne
        """
        # logger.info('query ids')
        if len(id_list) > 0:
            response = self.__tweepy_client.get_tweets(
                ids=id_list,
                expansions='geo.place_id',
                tweet_fields='id,text,lang,source,created_at,geo',
                user_fields=None,
                place_fields='country,country_code,geo,name'
            )

            if response.data is None:
                logger.warning('get an Empty response from query ids')
                return

            # Location in melbourne?
            if response.includes is not None and response.includes.get('places') is not None:
                places = response.includes.get('places')
                logger.debug('place record exist: ' + str(places))

                for place in places:
                    # melbourne condition
                    is_result_set_contains_melbourne_res = place.get('id') == MELBOURNE_PLACE_ID \
                                                           or place.get('name').lower() == 'melbourne' \
                                                           or place.get('full_name').lower() == 'melbourne'

                    if is_result_set_contains_melbourne_res:
                        logger.debug('passed place filter')

                        raw_twitters = response.data
                        # find all melbourne raw_twitters
                        for raw_twitter in raw_twitters:
                            # melbourne condition for each tweet
                            is_tweet_from_melbourne = raw_twitter.get('geo') is not None \
                                                      and raw_twitter.get('geo').get('place_id') == MELBOURNE_PLACE_ID

                            if is_tweet_from_melbourne:
                                logger.debug('passed geo filter')
                                # language filter
                                if self.__config.is_fetch_english_tweet_only() and not is_tweet_english(raw_twitter):
                                    continue

                                logger.debug('passed lang filter')

                                full_text = twitter_preprocess_helper.get_full_text(raw_twitter)
                                logger.debug('full text: ' + full_text)

                                # keyword filter
                                if not keyword_helper.is_text_match_keywords(full_text):
                                    continue

                                logger.debug('passed keyword filter')
                                tweet_dict_for_storage = twitter_preprocess_helper.preprocess_twitter(raw_twitter)

                                # put it to db
                                self.__db_helper.put_twitter_to_db(tweet_dict_for_storage)

                        # have found all melbourne tweets in this batch, exit place loop
                        break

    def run(self) -> None:
        while True:

            try:
                twitter_id = self.__queue.get_twitter_id_from_queue()
                self.__push_id_to_search(twitter_id)

            except Empty as empty_queue_exception:
                # if the producer has been finished, gracefully exit
                if self.__end_signal_helper.is_end_of_id_file():
                    # handle rest query
                    # self.__query_ids_located_in_melbourne(self.__id_list)
                    self.__query_ids_mentioned_melbourne(self.__id_list)

                    logger.success('Successfully handled all tweet IDs')
                    break
                else:
                    logger.warning('TwitterIdQueue is empty for too long time')
                    continue


if __name__ == '__main__':
    # test
    elements = None
