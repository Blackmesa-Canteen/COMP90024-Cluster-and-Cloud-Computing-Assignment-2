import json
import time

import fuzzywuzzy.fuzz
import tweepy

# TODO 完成此处
from loguru import logger

from common_util.config_handler import ConfigHandler


class TwitterStream(tweepy.Stream):
    """
    author: xiaotian li
    """

    def __init__(self,
                 consumer_key,
                 consumer_secret,
                 access_token,
                 access_token_secret,
                 queue
                 ):

        tweepy.Stream.__init__(self,
                               consumer_key=consumer_key,
                               consumer_secret=consumer_secret,
                               access_token=access_token,
                               access_token_secret=access_token_secret
                               )
        self.__queue = queue

    def on_data(self, raw_data):
        try:
            # filter key words
            tweet_json_data = json.loads(raw_data)
            print(tweet_json_data)

            # unify text attribute
            if "full_text" in tweet_json_data:
                tweet_json_data["text"] = tweet_json_data["full_text"]

            # get the full text
            if tweet_json_data["truncated"]:
                tweet_json_data["text"] = tweet_json_data["extended_tweet"]["full_text"]

            # match keywords
            config = ConfigHandler()
            key_word_sentence = config.get_lower_key_word_token_string()

            ratio = fuzzywuzzy.fuzz.token_set_ratio(key_word_sentence, tweet_json_data["text"])
            logger.debug("match score: " + str(ratio) + " in text: " + tweet_json_data["text"])
            if ratio >= config.get_key_word_match_degree():
                # matched twitter into queue
                self.__queue.put_twitter_doc_in_queue(twitter_doc=tweet_json_data)

        except BaseException as e:
            logger.debug(raw_data)
            logger.error(e)
            return True

        return True

    def on_status(self, status):
        pass

    def on_request_error(self, status_code):
        print(status_code)

        if status_code == 420:
            time.sleep(5)
        if status_code == 429:
            logger.debug("Waiting on limit")
            time.sleep(10 * 60)
        else:
            logger.debug("unexpected error. See error code above. Retry in 10 s")
            time.sleep(5)


if __name__ == '__main__':
    print(" ".join(["abb", "asd", "fgdf", "fgf"]))
