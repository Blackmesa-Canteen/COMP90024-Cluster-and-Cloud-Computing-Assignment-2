# author: xiaotian Li
import threading

from db_util.db_helper import DbHelper
from twitter_util.twitter_preprocess_helper import preprocess_twitter


class TwitterDbStorageConsumer(threading.Thread):
    """
    author: xiaotian li
    """

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.__q = queue
        self.__db_helper = DbHelper()

    def run(self) -> None:

        # constantly consume the queue, preprocess db and put data into db
        while True:
            raw_twitter_doc = self.__q.get_twitter_doc_from_queue()

            # normalize before put to db
            original_twitter_doc = raw_twitter_doc['data']
            twitter_doc_to_storage = preprocess_twitter(original_twitter_doc)

            self.__db_helper.put_twitter_to_db(
                twitter_doc_to_storage
            )

