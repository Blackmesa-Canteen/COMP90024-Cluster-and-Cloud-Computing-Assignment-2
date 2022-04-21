from common_util.config_handler import ConfigHandler
from historical_twitter_util.historical_twitter_handler import HistoricalTwitterHandler


class HistoryTweetCrawler:
    """
    get environment related tweets and put them in the CouchDB

    author: Xiaotian Li
    """

    def __init__(self):
        pass

    def run(self):
        handler = HistoricalTwitterHandler()
        handler.parse_twitter_with_keyword_and_put_to_db()
