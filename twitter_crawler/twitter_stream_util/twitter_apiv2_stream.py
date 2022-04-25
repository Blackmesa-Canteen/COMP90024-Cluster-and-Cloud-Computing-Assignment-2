import json
import time

import tweepy
from fuzzywuzzy import fuzz
from loguru import logger

from common_util.config_handler import ConfigHandler


class TwitterV2Stream(tweepy.StreamingClient):

    def __init__(self,
                 bearer_token,
                 queue
                 ):

        tweepy.StreamingClient.__init__(self,
                                        bearer_token=bearer_token,
                                        wait_on_rate_limit=True
                                        )
        self.__queue = queue

    def on_data(self, raw_data):
        """

        :param raw_data: raw data received from twitter
        {
            "data": {
            "created_at": "2022-04-21T01:42:22.000Z",
            "geo": {},
            "id": "1516955469935349760",
            "lang": "en",
            "source": "Twitter for iPhone",
            "text": "RT @Sarah77414568: This weekend in Melbourne I can stand at a bar and order a drink with No Vax Passport BUT I can\'t stand behind a bar and\xe2\x80\xa6"
                },

            "matching_rules": [{
                "id": "1516955317023940609",
                "tag": "tweets about keywords in melbourne"
            }]
        }
        :return:
        """
        try:

            # parse income into dict
            raw_data_doc = json.loads(raw_data)
            self.__queue.put_twitter_doc_in_queue(raw_data_doc)

        except BaseException as e:
            logger.debug(raw_data)
            logger.exception(e)
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
