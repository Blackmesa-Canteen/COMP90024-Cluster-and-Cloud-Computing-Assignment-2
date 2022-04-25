# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     main_app.py
   Description :  main entrance of the tweet crawler

   There are 3 scenarios:

   1 - Stream new tweets in melbourne into db, running forever
   2 - Search covid-19 related tweet in melbourne in 2020 based on local tweet IDs, then put it into db
   3-  Fetch historical (2014-2017) tweets in melbourne from local file, then put it into db

   Author :       Xiaotian Li
   date：          14/04/2022
-------------------------------------------------
"""
from optparse import OptionParser

from loguru import logger

from crawlers.covid_search_crawler import CovidSearchCrawler
from crawlers.history_tweet_crawler import HistoryTweetCrawler
from crawlers.twitter_stream_crawler import TwitterStreamCrawler
from common_util.config_handler import ConfigHandler
from nlp_util.sentiment_helper import SentimentHelper

S_1_CONFIG_FILE_NAME = "app_twitter_stream_config.yaml"
S_2_CONFIG_FILE_NAME = "app_covid_search_config.yaml"
S_3_CONFIG_FILE_NAME = "app_history_tweet_config.yaml"

if __name__ == '__main__':

    # arg parser
    parser = OptionParser(usage="usage:%prog -s [scenario number]")
    parser.add_option("-s", "--scenario",
                      action="store",
                      type='int',
                      dest="scenario",
                      default=1,
                      help="Specify scenario to run the crawler, see comment in the main_app.py"
                      )

    (options, args) = parser.parse_args()

    if options.scenario:
        config = ConfigHandler()
        choice = options.scenario

        # init Sentiment helper first:
        SentimentHelper()

        if choice == 1:
            logger.info('Scenario 1 running: Stream new tweets in melbourne into db, running forever')
            handler = TwitterStreamCrawler()
            # set config file
            config.reset_config_file_name(S_1_CONFIG_FILE_NAME)
            handler.run(
                twitter_fetch_thread_num=1,
                db_consumer_thread_num=1
            )

        elif choice == 2:
            logger.info('Scenario 2 running: Search covid-19 related tweet in melbourne in 2020 based on '
                        'local tweet IDs, then put it into db')

            data_dirs = ['2020-01', '2020-02', '2020-03', '2020-04', '2020-05', '2020-06', '2020-07', '2020-08',
                         '2020-09', '2020-10', '2020-11', '2020-12']

            handler = CovidSearchCrawler(data_dirs=data_dirs)
            # set config file
            config.reset_config_file_name(S_2_CONFIG_FILE_NAME)
            handler.run(
                search_consumer_thread_num=5
            )

        elif choice == 3:
            logger.info('Scenario 3 running:  Fetch historical (2014-2017) tweets in melbourne from local file, '
                        'then put it into db')

            handler = HistoryTweetCrawler()
            # set config file
            config.reset_config_file_name(S_3_CONFIG_FILE_NAME)
            handler.run()

        else:
            logger.warning('Undefined scenario number: ' + choice)
            exit(-1)

        logger.success("crawler job's done")

    else:
        logger.error('Running arguments error.')
        logger.info('usage: python3 main_app.py -s [scenario number]')
        exit(-1)
