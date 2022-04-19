import os.path

import ijson
from loguru import logger

from common_util.config_handler import ConfigHandler
from db_util.db_helper import DbHelper
from twitter_util.twitter_preprocess_helper import preprocess_twitter

CONFIG = ConfigHandler()


class HistoricalTwitterHandler:

    def __init__(self):
        self.__historical_twitter_file_path = CONFIG.get_historical_tweet_file_path()
        self.__db_helper = DbHelper()

    def parse_twitter_and_put_to_db(self):
        """
        parse twitter JSON and put twitter to database

        author: xiaotian li
        """

        if not os.path.exists(self.__historical_twitter_file_path):
            logger.error('historical file path not exist: ' + self.__historical_twitter_file_path)
            exit(-1)

        with open(self.__historical_twitter_file_path, 'r', encoding='utf-8') as f:
            objects = ijson.items(f, 'rows.item')

            while True:
                try:
                    # preprocess to remove redundant information
                    original_tweet_dict = objects.__next__()['doc']
                    tweet_dict_for_storage = preprocess_twitter(original_tweet_dict)
                    print('*****************')
                    print(tweet_dict_for_storage)
                    print('*****************')


                except StopIteration as finish_e:
                    logger.success('finished parse local twitter')
                    break
                except Exception as e:
                    print(original_tweet_dict)
                    break

if __name__ == '__main__':
    handler = HistoricalTwitterHandler()
    handler.parse_twitter_and_put_to_db()
