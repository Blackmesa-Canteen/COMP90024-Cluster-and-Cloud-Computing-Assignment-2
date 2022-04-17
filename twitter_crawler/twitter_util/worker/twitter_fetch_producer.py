# author: xiaotian Li
import threading

import tweepy
from tweepy import Stream

from common_util.config_handler import ConfigHandler
from twitter_util.twitter_stream import TwitterStream


class TwitterFetchProducer(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)

        self.__q = queue
        self.__config = ConfigHandler()

    def run(self) -> None:
        """__init__( \
                    consumer_key, consumer_secret, access_token, access_token_secret, \
                    chunk_size=512, daemon=False, max_retries=inf, proxy=None, \
                    verify=True \
                )
                """
        stream = TwitterStream(
            consumer_key=self.__config.get_api_key(),
            consumer_secret=self.__config.get_api_secret(),
            access_token=self.__config.get_access_token(),
            access_token_secret=self.__config.get_access_token_secret()
        )

        # search in box, e.g. [112.28, -44.36, 155.23, -10.37]
        point_a = self.__config.get_target_box_point_a()
        point_b = self.__config.get_target_box_point_b()
        target_location_box = [
            point_a['longitude'],
            point_a['latitude'],
            point_b['longitude'],
            point_b['latitude']
        ]

        # set filter
        if self.__config.is_fetch_english_tweet_only():
            stream.filter(
                languages=["en"],
                track=self.__config.get_key_word_list(),
                locations=target_location_box
            )

        else:
            # no language restriction
            stream.filter(
                track=self.__config.get_key_word_list(),
                locations=target_location_box
            )


if __name__ == '__main__':
    # test
    config = ConfigHandler()
    auth = tweepy.OAuth1UserHandler(
        consumer_key=config.get_api_key(),
        consumer_secret=config.get_api_secret(),
        access_token=config.get_access_token(),
        access_token_secret=config.get_access_token_secret()
    )

    api = tweepy.API(auth)

    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)
