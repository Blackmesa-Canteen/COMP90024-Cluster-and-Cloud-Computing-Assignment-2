# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sentiment_analyser
   Description :  some static function for NLP
   Author :       Xiaotian Li
   date：          14/04/2022
-------------------------------------------------
"""
import nltk
from nltk.corpus import twitter_samples

import re
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer

from textblob import TextBlob


class SentimentHelper:
    # singleton
    __instance = None

    # singleton
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(SentimentHelper, cls).__new__(
                cls, *args, **kwargs)
            # init
            nltk.download('stopwords')

        return cls.__instance

    def __init__(self):
        pass

    def __get_sanitized_text(self, twitter_content_text):
        """
        sanitize twitter content with NLTK or something else:
            0. use regex to discard special characters: url, retweet(RT), @, #, etc...
            1. correct spell
            2. make sentence into word token
            3. remove stop words (oh, he, an...) with NLTK
            4. standardize words
            5. reconstruct strinh

        :param twitter_content_text: twitter content text
        :return: sanitized_text for sentiment method calling
        """

        # Remove the old style retweet text "RT"
        res = re.sub(r'^RT[\s]+', '', twitter_content_text)

        # Remove hyperlinks
        res = re.sub(r'https?:\/\/.*[\r\n]*', '', res)

        # it will remove hashtags
        # only removing the hash # sign from the word
        res = re.sub(r'#', '', res)

        # it will remove single numeric terms in the tweet.
        res = re.sub(r'[0-9]', '', res)

        # correct spellings
        res = str(TextBlob(res).correct())

        # instantiate the tokenizer class
        tokenizer = TweetTokenizer(preserve_case=False,
                                   strip_handles=True,
                                   reduce_len=True)

        # tokenize the tweets
        tweet_tokens = tokenizer.tokenize(res)

        # remove some stop words and punctuations
        tweets_clean = []
        stopwords_english = stopwords.words('english')

        for word in tweet_tokens:  # Go through every word in your tokens list
            if (word not in stopwords_english and  # remove stopwords
                    word not in string.punctuation):  # remove punctuation
                tweets_clean.append(word)

        # standardize words: make ing, ed, t to normal form
        # Instantiate stemming class
        stemmer = PorterStemmer()

        # Create an empty list to store the stems
        tweets_stem = []

        for word in tweets_clean:
            stem_word = stemmer.stem(word)  # stemming word
            tweets_stem.append(stem_word)  # append to the list

        return " ".join(map(str, tweets_stem))

    def get_polarity_from_text(self, twitter_text):
        """
        get polarity (The emotion score is a float within the range [-1.0, 1.0])

        :param twitter_content_text
        :return: The emotion score is a float within the range [-1.0, 1.0]
        """
        purified_text = self.__get_sanitized_text(twitter_text)
        return TextBlob(purified_text).polarity

    def get_subjectivity_from_text(self, twitter_text):
        """
            get subjectivity.

            :param twitter_content_text

            :return: The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very
            objective and 1.0 is very subjective
            """
        purified_text = self.__get_sanitized_text(twitter_text)
        return TextBlob(purified_text).subjectivity


# test can run here
if __name__ == '__main__':
    helper = SentimentHelper()
    text = "Who Wouldn't Love These Big....Juicy....Selfies :) - http://t.co/QVzjgd1uFo http://t.co/oWBL11eQRY"
    print(text)
    print(helper.get_polarity_from_text(text))
