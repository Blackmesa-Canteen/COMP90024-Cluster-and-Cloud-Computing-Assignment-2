import tweepy

# TODO 完成此处
class TwitterApiListener(tweepy.Stream):
    """
    author: xiaotian li
    """

    def on_data(self, raw_data):
        pass

    def on_status(self, status):
        pass

    def on_request_error(self, status_code):
        pass
