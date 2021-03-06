import os.path

import ijson
from loguru import logger
from lxml import etree

from common_util.config_handler import ConfigHandler
from db_util.db_helper import DbHelper
from twitter_util.twitter_preprocess_helper import preprocess_twitter, get_full_text, is_tweet_english
from twitter_util.keyword_helper import is_text_match_keywords

CONFIG = ConfigHandler()


class HistoricalTwitterHandler:

    def __init__(self):
        self.__historical_twitter_file_path = CONFIG.get_historical_tweet_file_path()
        self.__db_helper = DbHelper()

    def parse_all_twitter_and_put_to_db(self):
        """
        parse all twitter JSON and put twitter to database

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

                    # language filter
                    if CONFIG.is_fetch_english_tweet_only() and not is_tweet_english(original_tweet_dict):
                        continue

                    tweet_dict_for_storage = preprocess_twitter(original_tweet_dict)

                    self.__db_helper.put_twitter_to_db(tweet_dict_for_storage)

                except StopIteration as finish_e:
                    logger.success('finished parse local twitter')
                    break
                except Exception as e:
                    print(original_tweet_dict)
                    logger.exception(e)
                    break

    def parse_twitter_with_keyword_and_put_to_db(self):
        """
        parse twitter about some keywords and put twitter to database

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
                    full_text = get_full_text(original_tweet_dict)

                    # language filter
                    if CONFIG.is_fetch_english_tweet_only() and not is_tweet_english(original_tweet_dict):
                        continue

                    # keyword filter
                    if not is_text_match_keywords(full_text):
                        continue

                    # fix: handle source html text
                    try:
                        if original_tweet_dict.get('source') is not None:
                            html = original_tweet_dict.get('source')
                            _element = etree.HTML(html)
                            original_tweet_dict['source'] = _element.xpath('//a/text()')[0]
                    except:
                        original_tweet_dict['source'] = 'unknown'

                    tweet_dict_for_storage = preprocess_twitter(original_tweet_dict)
                    self.__db_helper.put_twitter_to_db(tweet_dict_for_storage)

                except StopIteration as finish_e:
                    logger.success('finished parse local twitter')
                    break
                # except Exception as e:
                #     break


if __name__ == '__main__':
    # test
    handler = HistoricalTwitterHandler()
    handler.parse_twitter_with_keyword_and_put_to_db()
