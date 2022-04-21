import threading
from queue import Empty

import tweepy
from loguru import logger

from common_util.config_handler import ConfigHandler
from covid_twitter_util.worker import twitter_hydrate_producer
from twitter_util.twitter_preprocess_helper import is_tweet_english

MELBOURNE_PLACE_ID = '01864a8a64df9dc4'

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

        # api authentication
        self.__tweepy_client = tweepy.Client(
            bearer_token=self.__config.get_api_token(),
            wait_on_rate_limit=True
        )

    def __push_id_to_search(self, tweet_id):
        """
        queue size is 100, if the queue size reaches 100, query 100 ids with API, then clear queue for next
        100.
        This logic is created because of twitter api's 100 ID query limitation
        :param tweet_id:
        :return: null

        author: xiaotian li
        """

        if len(self.__id_list) >= 100:
            # query 100 ids each time
            self.__query_ids(self.__id_list)
            # free the queue
            del self.__id_list
            self.__id_list = []
        else:
            self.__id_list.append(str(tweet_id))

    def __query_ids(self, id_list):
        """
        handle response
        """
        if len(id_list) > 0:
            logger.info('query id length ' + str(len(id_list)))
            response = self.__tweepy_client.get_tweets(
                ids=id_list,
                expansions='geo.place_id',
                tweet_fields='id,text,lang,source,created_at,geo',
                user_fields=None,
                place_fields='country,country_code,geo,name'
            )

            # Location in melbourne?
            if response.get('includes') is not None and response.get('includes').get('places') is not None:
                places = response.get('includes').get('places')
                # check places exist melbourne or not
                for place in places:
                    if place.get('id') == MELBOURNE_PLACE_ID or place.get('name') == 'melbourne':
                        # melbourne twitter exists, locate it:
                        raw_twitters = response.get('data')

                        for raw_twitter in raw_twitters:
                            if raw_twitter.get('geo') is not None \
                                and raw_twitter.get('geo').get('place_id') == MELBOURNE_PLACE_ID:

                                # language filter
                                if self.__config.is_fetch_english_tweet_only() and not is_tweet_english(raw_twitter):
                                    continue

                                # TODO preprocess this twitter
                                print(raw_twitter)


    def run(self) -> None:
        while True:

            try:
                twitter_id = self.__queue.get_twitter_id_from_queue()
                self.__push_id_to_search(twitter_id)

            # TODO: End logic
            except Empty as empty_queue_exception:
                # if the producer has been finished, gracefully exit
                if self.__end_signal_helper.is_end_of_id_file():
                    # handle rest query
                    self.__query_ids(self.__id_list)

                    logger.success('Successfully handled all tweet IDs')
                    break
                else:
                    logger.warning('TwitterIdQueue is empty for too long time')
                    continue


if __name__ == '__main__':
    elements = None

    for i in elements:
        print()