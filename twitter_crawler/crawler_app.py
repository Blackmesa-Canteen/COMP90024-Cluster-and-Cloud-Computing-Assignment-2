# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crawler_app.py
   Description :  main entrance of the tweet crawler

   There are 3 scenarios:

   1 - Stream new tweets in melbourne into db, running forever
   2 - Search covid-19 related tweet in melbourne in 2020 based on local tweet IDs, then put it into db
   3- Fetch all environment related historical tweets in melbourne from local file, then put it into db

   Author :       Xiaotian Li
   date：          14/04/2022
-------------------------------------------------
"""
import sys
from optparse import OptionParser

from loguru import logger

from apps.history_tweet_crawler import HistoryTweetCrawler
from common_util.config_handler import ConfigHandler

S_3_CONFIG_FILE_NAME = "app_history_tweet_config.yaml"

if __name__ == '__main__':

    # arg parser
    parser = OptionParser(usage="usage:%prog -s [scenario number]")
    parser.add_option("-s", "--scenario",
                      action="store",
                      type='int',
                      dest="scenario",
                      default=0,
                      help="Specify scenario to run the crawler, see comment in the crawler_app.py"
                      )

    (options, args) = parser.parse_args()

    if options.scenario:
        config = ConfigHandler()
        choice = options.scenario

        if choice == 1:
            logger.info('Scenario 1 running: Stream new tweets in melbourne into db, running forever')

        elif choice == 2:
            logger.info('Scenario 2 running: Search covid-19 related tweet in melbourne in 2020 based on '
                        'local tweet IDs, then put it into db')

        elif choice == 3:
            logger.info('Scenario 3 running:  all environment related historical tweets in melbourne from local file, '
                        'then put it into db')

            handler = HistoryTweetCrawler()
            config.reset_config_file_name(S_3_CONFIG_FILE_NAME)
            handler.run()

        else:
            logger.warning('Undefined scenario number: ' + choice)
            exit(0)

    else:
        logger.error('Running arguments error.')
        logger.info('usage: python3 crawler_app.py -s [scenario number]')
        exit(-1)
