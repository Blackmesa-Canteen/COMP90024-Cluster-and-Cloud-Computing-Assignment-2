import gzip
import os
import threading

from loguru import logger
from pathlib import Path

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

    def __parse_id_file_and_search(self, file_path):
        with gzip.open(file_path, 'rt', encoding='utf-8') as f:
            for line in f:
                line = line.strip('\n')

                # put one id into a queue
                self.__queue.put_twitter_id_in_queue(line)

    def run(self) -> None:
        for data_dir in self.__data_dirs:
            data_dir = os.path.join(self.__config.get_covid_tweet_id_file_path(), data_dir)
            for file_path in Path(data_dir).iterdir():
                if file_path.name.endswith('.gz'):
                    self.__parse_id_file_and_search(file_path)

        # set end signal
        self.__end_signal_helper.set_end_of_id_file_signal(True)
