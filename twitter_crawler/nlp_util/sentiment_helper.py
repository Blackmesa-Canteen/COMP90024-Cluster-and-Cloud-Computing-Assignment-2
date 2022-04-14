# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sentiment_analyser
   Description :  some static function for NLP
   Author :       Xiaotian Li
   date：          14/04/2022
-------------------------------------------------
"""
from textblob import TextBlob

def get_sanitized_text(twitter_content_text):
    """
    sanitize twitter content with NLTK or something else:
        1. use regex to discard special characters: url, retweet(RT), @, #, etc...
        2. Convert char into lowercase, remove stop words (oh, he, an...) with NLTK
    :param twitter_content_text: twitter content text
    :return: sanitized_text for sentiment method calling
    """
    pass

def get_polarity_from_text(sanitized_text):
    """
    get polarity (The emotion score is a float within the range [-1.0, 1.0])

    :param sanitized_text: input text need to be filtered!
        before calling the method, please do something to the input text first:
        1. using regex to discard special characters: url, retweet(RT), @, #, etc...
        2. Convert char into lowercase, remove stop words (oh, he, an...) with NLTK
        3. Then, you can pass the text into this function to get result
    :return: The emotion score is a float within the range [-1.0, 1.0]
    """
    return TextBlob(sanitized_text).polarity


def get_subjectivity_from_text(sanitized_text):
    """
        get subjectivity.

        :param sanitized_text: input text need to be filtered!
            before calling the method, please do something to the input text first:
            1. using regex to discard special characters: url, retweet(RT), @, #, etc...
            2. Convert char into lowercase, remove stop words (oh, he, an...) with NLTK
            3. Then, you can pass the text into this function to get result

        :return: The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very
        objective and 1.0 is very subjective
        """
    return TextBlob(sanitized_text).subjectivity


# test can run here
if __name__ == '__main__':
    pass
