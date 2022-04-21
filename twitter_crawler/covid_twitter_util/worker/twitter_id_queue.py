import queue

from common_util.config_handler import ConfigHandler

# 15 min
BLOCK_TIME_FOR_GET = 900

class TwitterIdQueue:
    """
        Time decoupling is achieved using the publisher/subscriber pattern
        author: Xiaotian Li
        """
    # singleton
    __instance = None

    # singleton
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(TwitterIdQueue, cls).__new__(
                cls, *args, **kwargs)

            # init
            self = cls.__instance
            self.__config = ConfigHandler()
            self.__q_size = self.__config.get_block_queue_size()
            self.__q = queue.Queue(self.__q_size)

        return cls.__instance

    def put_twitter_id_in_queue(self, twitter_doc):
        self.__q.put(twitter_doc, block=True, timeout=None)

    def get_twitter_id_from_queue(self):
        return self.__q.get(block=True, timeout=BLOCK_TIME_FOR_GET)

    def get_queue_size(self):
        return self.__q.qsize()
