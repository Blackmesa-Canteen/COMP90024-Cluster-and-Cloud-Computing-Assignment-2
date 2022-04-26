# author: xiaotian Li
import threading

import tweepy
from loguru import logger
from tweepy import Stream

from common_util.config_handler import ConfigHandler
from twitter_stream_util.twitter_apiv2_stream import TwitterV2Stream
from twitter_stream_util.twitter_stream import TwitterStream


class TwitterFetchProducer(threading.Thread):
    """
    Time decoupling is achieved using the publisher/subscriber pattern
    author: Xiaotian Li
    """

    def __init__(self, queue):
        threading.Thread.__init__(self)

        self.__q = queue
        self.__config = ConfigHandler()

    def run(self) -> None:

        # twitter api v1 is not supported
        if self.__config.get_api_level() == 1:

            # stream = TwitterStream(
            #     consumer_key=self.__config.get_api_key(),
            #     consumer_secret=self.__config.get_api_secret(),
            #     access_token=self.__config.get_access_token(),
            #     access_token_secret=self.__config.get_access_token_secret(),
            #     queue=self.__q
            # )
            #
            # # search in box, e.g. [112.28, -44.36, 155.23, -10.37]
            # point_a = self.__config.get_target_box_point_a()
            # point_b = self.__config.get_target_box_point_b()
            # target_location_box = [
            #     point_a['longitude'],
            #     point_a['latitude'],
            #     point_b['longitude'],
            #     point_b['latitude']
            # ]
            #
            # # set filter
            # # can NOT use both keyword track and location! we filter the search_word later in the StreamListenerConsumer
            # if self.__config.is_fetch_english_tweet_only():
            #     stream.filter(
            #         languages=["en"],
            #         locations=target_location_box
            #     )

            logger.warning("twitter api v1 is not supported!")
            exit(-1)

        # twitter stream api v2
        else:
            if not config.get_academic_access():
                self.stream_without_academic_account()
            else:
                self.stream_with_academic_account()


    def stream_without_academic_account(self):
        """
        If you don't have elevated level, please use this method

        """
        key_word_list = self.__config.get_key_word_list()
        # location rule: melbourne
        # avaliable only for research access level
        # self.__rule = tweepy.StreamRule(
        #     value="place:melbourne",
        #     tag="tweets in melbourne"
        # )
        # altenative location rule: melbourne
        if len(key_word_list) != 0:

            keyword_string = "(#melbourne OR #Melbourne) ("

            # keywords
            processed_keyword_list = []
            for keyword in key_word_list:
                keyword_string = \
                    keyword_string \
                    + '"' \
                    + keyword \
                    + '"' \
                    + ' OR '

            # remove redundant OR
            keyword_string = keyword_string[:-4]
            keyword_string = keyword_string + ')'

        else:
            keyword_string = "(#melbourne OR #Melbourne)"
        rule_text = keyword_string
        # language rule
        if self.__config.is_fetch_english_tweet_only():
            rule_text = rule_text + " lang:en"
        # build the rule
        logger.info('stream rule: ' + rule_text)
        stream_rule = tweepy.StreamRule(
            value=rule_text,
            tag="tweets about keywords in melbourne"
        )
        # setup stream
        stream = TwitterV2Stream(
            bearer_token=self.__config.get_api_token(),
            queue=self.__q
        )
        # link search rule
        stream.add_rules(stream_rule)
        # link output filter
        stream.filter(
            expansions="geo.place_id",
            tweet_fields=['id', 'text', 'lang', 'source', 'created_at', 'geo'],
            user_fields=None,
            place_fields=['country', 'country_code', 'geo', 'name'],
        )
        # then run forever to fetch new coming twitters

    def stream_with_academic_account(self):
        """
        If you don't have elevated level, please use this method

        """
        key_word_list = self.__config.get_key_word_list()
        if len(key_word_list) != 0:

            # can use geo keyword with elevated level
            keyword_string = "place:melbourne ("

            # keywords
            processed_keyword_list = []
            for keyword in key_word_list:
                keyword_string = \
                    keyword_string \
                    + '"' \
                    + keyword \
                    + '"' \
                    + ' OR '

            # remove redundant OR
            keyword_string = keyword_string[:-4]
            keyword_string = keyword_string + ')'

        else:
            keyword_string = "place:melbourne"
        rule_text = keyword_string
        # language rule
        if self.__config.is_fetch_english_tweet_only():
            rule_text = rule_text + " lang:en"
        # build the rule
        logger.info('stream rule: ' + rule_text)
        stream_rule = tweepy.StreamRule(
            value=rule_text,
            tag="tweets about keywords in melbourne"
        )
        # setup stream
        stream = TwitterV2Stream(
            bearer_token=self.__config.get_api_token(),
            queue=self.__q
        )
        # link search rule
        stream.add_rules(stream_rule)
        # link output filter
        stream.filter(
            expansions="geo.place_id",
            tweet_fields=['id', 'text', 'lang', 'source', 'created_at', 'geo'],
            user_fields=None,
            place_fields=['country', 'country_code', 'geo', 'name'],
        )
        # then run forever to fetch new coming twitters


if __name__ == '__main__':
    # test
    config = ConfigHandler()
    config.reset_config_file_name('app_twitter_stream_config.yaml')
    test = TwitterFetchProducer(queue=None)
    test.run()
