from loguru import logger

from nlp_util.sentiment_helper import SentimentHelper


def is_twitter_locate_in_target_box(self, original_twitter_doc):
    pass

def preprocess_twitter(original_twitter_doc):
    """
    preprocess the original twitter fetched to object that is suitable for database to store

    :param original_twitter_doc: original twitter obj
    :return: twitter_dict: the dict that is suitable for database to store

    author: xiaotian li
    """

    tweet_dict = dict()

    # set tweet id as document id
    tweet_dict["_id"] = str(original_twitter_doc["id"])

    # date: created_at : "Wed Jan 01 00:00:00 +0000 2020"
    tweet_dict["created_at"] = original_twitter_doc['created_at']

    # unify text attribute (already done in the stream)
    # if "full_text" in original_twitter_doc:
    #     tweet_dict["text"] = original_twitter_doc["full_text"]
    #
    # else:
    #     tweet_dict["text"] = original_twitter_doc["text"]

    # get the full text (already done in the stream)
    # if original_twitter_doc["truncated"]:
    #     tweet_dict["text"] = original_twitter_doc["extended_tweet"]["full_text"]

    # get language info
    if original_twitter_doc["metadata"] is not None and \
            original_twitter_doc["metadata"]["iso_language_code"] is not None:

        tweet_dict["iso_language_code"] = original_twitter_doc["metadata"]["iso_language_code"]
    else:
        tweet_dict["iso_language_code"] = "und"

    if original_twitter_doc["lang"] is not None:
        tweet_dict["lang"] = original_twitter_doc["lang"]
    else:
        tweet_dict["lang"] = "und"

    # get coordinates
    tweet_dict["coordinates"] = original_twitter_doc["coordinates"]

    # Do NLP process
    npl_helper = SentimentHelper()
    tweet_dict["purified_text"] = npl_helper.get_sanitized_text(tweet_dict["text"])
    tweet_dict["polarity"] = npl_helper.get_polarity_from_text(tweet_dict["purified_text"])
    tweet_dict["subjectivity"] = npl_helper.get_subjectivity_from_text(tweet_dict["purified_text"])

    tweet_dict["place"] = original_twitter_doc["place"]

    return tweet_dict

