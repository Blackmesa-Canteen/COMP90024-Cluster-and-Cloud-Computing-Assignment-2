import tweepy
from loguru import logger

from common_util.config_handler import ConfigHandler
from twitter_stream_util.worker.twitter_db_storage_consumer import TwitterDbStorageConsumer
from twitter_stream_util.worker.twitter_doc_queue import TwitterDocQueue
from twitter_stream_util.worker.twitter_fetch_producer import TwitterFetchProducer


class TwitterStreamCrawler:
    """
        stream latest tweets and put them in db
        This crawler will run forever to crawl latests

        author: Xiaotian Li
        """

    def __init__(self):
        # build up the rule:
        self.__queue = TwitterDocQueue()
        self.__consumer_threads = []
        self.__producer_threads = []

    def run(self,
            db_consumer_thread_num,
            twitter_fetch_thread_num
            ):

        if db_consumer_thread_num <= 0 or twitter_fetch_thread_num <= 0:
            logger.error('wrong thread number')
            exit(-1)

        for i in range(0, db_consumer_thread_num):
            db_consumer_thread = TwitterDbStorageConsumer(self.__queue)
            self.__consumer_threads.append(db_consumer_thread)

        for i in range(0, twitter_fetch_thread_num):
            twitter_fetch_thread = TwitterFetchProducer(self.__queue)
            self.__producer_threads.append(twitter_fetch_thread)

        # run all threads
        for thread in self.__consumer_threads:
            thread.start()
        logger.success('all consumer threads are running.')
        for thread in self.__producer_threads:
            thread.start()
        logger.success('all producer threads are running.')

        # block the main thread until all done
        # it seems that no one will stop
        for thread in self.__consumer_threads:
            thread.join()
        for thread in self.__producer_threads:
            thread.join()