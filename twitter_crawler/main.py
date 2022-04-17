# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     main.py
   Description :  TODO
   Author :       Xiaotian Li
   date：          14/04/2022
-------------------------------------------------
"""
from twitter_util.worker.twitter_doc_queue import TwitterDocQueue
from twitter_util.worker.twitter_fetch_producer import TwitterFetchProducer

if __name__ == '__main__':
    # start the crawler logic here
    tw_doc_queue = TwitterDocQueue()
    twitter_fetch_producer = TwitterFetchProducer(tw_doc_queue)

    twitter_fetch_producer.run()
    twitter_fetch_producer.join()
