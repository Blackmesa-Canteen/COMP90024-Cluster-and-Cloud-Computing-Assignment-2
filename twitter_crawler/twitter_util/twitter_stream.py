import json
import time

import tweepy


# TODO 完成此处
from loguru import logger


class TwitterStream(tweepy.Stream):
    """
    author: xiaotian li
    """

    def on_data(self, raw_data):
        try:
            print(raw_data)

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
