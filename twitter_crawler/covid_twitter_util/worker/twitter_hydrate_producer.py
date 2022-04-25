import gzip
import os
import threading

from loguru import logger
from pathlib2 import Path

from common_util.config_handler import ConfigHandler

END_SIGNAL_TEXT = "END_OF_THE_ID_SEARCH"


class TwitterHydrateProducer(threading.Thread):
    """
    producer: read tweet id into a queue
    """

    def __init__(self, data_dirs, queue, end_signal_helper):
        threading.Thread.__init__(self)
        self.__queue = queue
        self.__end_signal_helper = end_signal_helper

        self.__config = ConfigHandler()

        if not os.path.exists(self.__config.get_covid_tweet_id_file_path()):
            logger.error('covid-tweet-id-file-path error!')
            exit(-1)

        self.__data_dirs = data_dirs

    def run(self) -> None:
        helper_thread_list = []
        for data_dir in self.__data_dirs:
            data_dir = os.path.join(self.__config.get_covid_tweet_id_file_path(), data_dir)

            helper_thread = HelperSubThread(data_dir=data_dir, queue=self.__queue)
            helper_thread_list.append(helper_thread)

        for thread in helper_thread_list:
            thread.start()

        for thread in helper_thread_list:
            thread.join()

        # set end signal if finished all reading thread
        self.__end_signal_helper.set_end_of_id_file_signal(True)


class HelperSubThread(threading.Thread):
    """
    thread for reading each month
    """

    def __init__(self, data_dir, queue):
        threading.Thread.__init__(self)
        self.__queue = queue

        self.__config = ConfigHandler()
        if not os.path.exists(data_dir):
            logger.error('covid data dir error: ' + data_dir)
            exit(-1)

        self.__data_dir = data_dir

    def __parse_id_file_and_search(self, file_path):
        with gzip.open(file_path, 'rt', encoding='utf-8') as f:
            for line in f:
                line = line.strip('\n')

                # put one id into a queue
                self.__queue.put_twitter_id_in_queue(line)

    def run(self) -> None:
        for file_path in Path(self.__data_dir).iterdir():
            if file_path.name.endswith('.gz'):
                self.__parse_id_file_and_search(file_path)
