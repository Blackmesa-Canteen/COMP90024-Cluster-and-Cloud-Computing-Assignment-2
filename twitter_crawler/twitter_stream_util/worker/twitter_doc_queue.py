import queue
import threading
from common_util.config_handler import ConfigHandler


class TwitterDocQueue:
    # singleton
    __instance = None

    # singleton
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(TwitterDocQueue, cls).__new__(
                cls, *args, **kwargs)

            # init
            self = cls.__instance
            self.__config = ConfigHandler()
            self.__q_size = self.__config.get_block_queue_size()
            self.__q = queue.Queue(self.__q_size)

        return cls.__instance

    def put_twitter_doc_in_queue(self, twitter_doc):
        """
        put twitter doc in doc,
        if queue is full, block the producer thread

        :param twitter_doc:
        """
        self.__q.put(twitter_doc, block=True, timeout=None)

    def get_twitter_doc_from_queue(self):
        """
        get twitter doc from queue,
        if the queue is empty, block consumer thread
        """
        return self.__q.get(block=True, timeout=None)

