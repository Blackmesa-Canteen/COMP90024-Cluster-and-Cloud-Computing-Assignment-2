import re
from datetime import datetime

from loguru import logger

from common_util import config_handler
from common_util.config_handler import ConfigHandler
from nlp_util.sentiment_helper import SentimentHelper

CONFIG = ConfigHandler()


def check_date_str_match_iso8601(date_text):
    regex = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?$'
    match_iso8601 = re.compile(regex).match
    try:

        if match_iso8601(date_text) is not None:
            return True
    except:
        pass
    return False


def datetime_object_to_string(datetime_obj):
    """
    take in a date time object, returns text:

    :param datetime_obj: datime object
    :return:
    """
    s = datetime_obj.strftime("%Y-%m-%dT%H:%M:%S.%f")
    return s[:-3] + 'Z'


def parse_tweet_date_to_iso8601(tweet_date_text):
    return datetime.strftime(datetime.strptime(tweet_date_text, '%a %b %d %H:%M:%S +0000 %Y'), '%Y-%m-%dT%H:%M:%S.000Z')


def get_full_text(original_twitter_doc):
    """
    quickly get full text from original twitter

    :param original_twitter_doc:
    :return: full text

    author: xiaotian li
    """
    res = original_twitter_doc["text"]
    if "full_text" in original_twitter_doc:
        res = original_twitter_doc["full_text"]

    # get the full text
    if original_twitter_doc.get("truncated") is not None and original_twitter_doc["truncated"]:
        if original_twitter_doc.get("extended_tweet") is not None:
            res = original_twitter_doc["extended_tweet"]["full_text"]
        elif original_twitter_doc.get("full_text") is not None:
            res = original_twitter_doc["full_text"]

    return res


def get_lang(original_twitter_doc):
    """
    get lang code

    :param original_twitter_doc:
    :return:
    """
    if original_twitter_doc.get("lang") is not None:
        return original_twitter_doc["lang"]

    elif original_twitter_doc.get("metadata") is not None and \
            original_twitter_doc["metadata"].get("iso_language_code") is not None:
        return original_twitter_doc["metadata"]["iso_language_code"]
    else:
        return "und"


def is_tweet_english(original_twitter_doc):
    return get_lang(original_twitter_doc) == "en"


def preprocess_twitter(original_twitter_doc):
    """
    preprocess the original twitter fetched to object that is suitable for database to store

    :param original_twitter_doc: original twitter json doc
    :return: twitter_dict: the dict that is suitable for database to store
    {
        '_id': '493805281185263600',
        'id': '493805281185263600',
        'created_at': "2022-04-21T01:42:22.000Z",
        'text': 'What? Boiled Milk? You mean.... Burnt milk. *facepalm*',
        'lang': 'en',
        'coordinates': {
            'type': 'Point',
            'coordinates': [145.2093684, -37.8145959]
        },
        'source' : "Twitter for iPhone",
        'polarity': -0.3125,
        'subjectivity': 0.6875
    }

    author: xiaotian li
    """

    tweet_dict = dict()

    # set tweet id as document id
    if original_twitter_doc.get('id') is not None:
        tweet_dict["_id"] = str(original_twitter_doc["id"])

    else:
        tweet_dict["_id"] = str(original_twitter_doc["_id"])
    tweet_dict["id"] = tweet_dict["_id"]

    # stream: ISO8601:  "2022-04-21T01:42:22.000Z"
    # history: Twitter format: "Mon Jul 28 17:03:36 +0000 2014"
    # covid: datetime: datetime(2020-01-29 18:11:15+00:00)
    if isinstance(original_twitter_doc['created_at'], datetime):
        # if the record is datetime object
        tweet_dict["created_at"] = datetime_object_to_string(original_twitter_doc['created_at'])
    else:
        if check_date_str_match_iso8601(original_twitter_doc['created_at']):
            # if already obey the ISO8601
            tweet_dict["created_at"] = original_twitter_doc['created_at']
        else:
            tweet_dict["created_at"] = parse_tweet_date_to_iso8601(original_twitter_doc['created_at'])

    # unify text attribute
    tweet_dict["text"] = get_full_text(original_twitter_doc)

    # get language info
    tweet_dict["lang"] = get_lang(original_twitter_doc)

    # get coordinates
    is_coor_exist = original_twitter_doc.get("coordinates") is not None
    if is_coor_exist and original_twitter_doc.get("coordinates")['type'] == 'Point':
        longitude = float(original_twitter_doc["coordinates"]["coordinates"][0])
        latitude = float(original_twitter_doc["coordinates"]["coordinates"][1])
        tweet_dict["coordinates"] = {
            'type': 'Point',
            'coordinates': [longitude, latitude]
        }
    elif original_twitter_doc.get("geo") is not None and original_twitter_doc.get("geo").get("coordinates") is not None:
        coordinate_obj = original_twitter_doc.get("geo").get("coordinates")
        coordinate_arr = coordinate_obj.get('coordinates')
        if coordinate_arr is not None:
            longitude = float(coordinate_arr[0])
            latitude = float(coordinate_arr[1])
        else:
            longitude = 144.9631
            latitude = 37.8136
        tweet_dict["coordinates"] = {
            'type': 'Point',
            'coordinates': [longitude, latitude]
        }
    else:
        # default coordinates
        tweet_dict["coordinates"] = {
            'type': 'Point',
            'coordinates': [144.9631, 37.8136]
        }

    # record source:
    if original_twitter_doc.get('source') is not None:
        tweet_dict['source'] = original_twitter_doc.get('source')
    else:
        tweet_dict['source'] = 'unknown'

    # Do NLP process
    npl_helper = SentimentHelper()

    # only do NLP on english twitter
    if tweet_dict["lang"] == 'en':
        purified_text = npl_helper.get_sanitized_text(tweet_dict["text"])
        tweet_dict["polarity"] = npl_helper.get_polarity_from_text(purified_text)
        tweet_dict["subjectivity"] = npl_helper.get_subjectivity_from_text(purified_text)
    else:
        tweet_dict["purified_text"] = ""
        tweet_dict["polarity"] = 0.0
        tweet_dict["subjectivity"] = 0.0

    # tweet_dict["place"] = original_twitter_doc["place"]

    return tweet_dict


if __name__ == '__main__':
    # test
    text = '2022-04-22T13:21.563Z'
    text2 = '2022-04-21T01:42:22.22233'
    datetime_obj = datetime.now()

    print(check_date_str_match_iso8601(datetime_object_to_string(datetime_obj)))

    print(check_date_str_match_iso8601(parse_tweet_date_to_iso8601('Mon Jul 28 17:08:48 +0000 2014')))
