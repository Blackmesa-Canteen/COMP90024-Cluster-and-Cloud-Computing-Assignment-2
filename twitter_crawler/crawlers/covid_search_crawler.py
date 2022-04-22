from loguru import logger

from covid_twitter_util.end_signal_helper import EndSignalHelper
from covid_twitter_util.worker.twitter_hydrate_producer import TwitterHydrateProducer
from covid_twitter_util.worker.twitter_id_queue import TwitterIdQueue
from covid_twitter_util.worker.twitter_id_search_consumer import TwitterIdSearchConsumer


class CovidSearchCrawler:
    """
    search covid related tweets by IDs that are provided by an opensource research project.
    We have 2020 year's tweet IDs, and search tweets from melbourne

    author: xiaotian li
    """

    def __init__(self, data_dirs):
        self.__queue = TwitterIdQueue()
        self.__consumer_threads = []
        self.__end_signal_helper = EndSignalHelper()
        self.__data_dirs = data_dirs

    def run(self,
            search_consumer_thread_num,
            ):

        if search_consumer_thread_num <= 0:
            logger.error('wrong thread number')
            exit(-1)

        for i in range(0, search_consumer_thread_num):

            search_consumer_thread = TwitterIdSearchConsumer(
                queue=self.__queue,
                end_signal_helper=self.__end_signal_helper
            )
            self.__consumer_threads.append(search_consumer_thread)

        # there will be only one producer thread
        hydrate_producer_thread = TwitterHydrateProducer(
            queue=self.__queue,
            end_signal_helper=self.__end_signal_helper,
            data_dirs=self.__data_dirs
        )

        # run threads

        for thread in self.__consumer_threads:
            thread.start()
        logger.success('all consumer threads are running.')

        hydrate_producer_thread.start()
        logger.success('the producer threads are running.')

        # wait all thread ends
        hydrate_producer_thread.join()
        for thread in self.__consumer_threads:
            thread.join()

        logger.success("Finished search covid tweets")