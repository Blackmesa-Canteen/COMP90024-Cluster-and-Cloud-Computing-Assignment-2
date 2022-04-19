from common_util.config_handler import ConfigHandler
from historical_twitter_util.historical_twitter_handler import HistoricalTwitterHandler

CONFIG_FILE_NAME = "app_history_environment_tweet_config.yaml"


class HistoryEnvironmentTweetCrawler:
    """
    get environment related tweets and put them in the CouchDB

    author: Xiaotian Li
    """

    def __init__(self):
        self.__config = ConfigHandler()
        self.__config.reset_config_file_name(CONFIG_FILE_NAME)

    def run(self):
        handler = HistoricalTwitterHandler()
        handler.parse_twitter_with_keyword_and_put_to_db()
