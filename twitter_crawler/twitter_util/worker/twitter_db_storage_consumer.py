# author: xiaotian Li
import threading


class TwitterDbStorageConsumer(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.__q = queue

    def run(self) -> None:
        pass
