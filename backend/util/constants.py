# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     constants
   Description :  some constants of database or views
   Author :       Xiaotian Li, Bocan Yang
   Date:          14/04/2022
-------------------------------------------------
"""

from itertools import count


covid_db_name = "covid-19-tweets"
all_tweets_db_name = "all-tweets"

income_api = {
   'position': ['income_by_pos', '1'],
   'year': ['income_by_year', '1'],
   'year-position': ['income_by_year_pos', '2'],
   'position-year': ['income_by_year_pos', '2']
}

hp_api = {
   'position': ['_avg_stat_by_pos', '1'],
   'year': ['_avg_stat_by_year', '1'],
   'type': ['_avg_stat_by_type', '1'],
   'type-position': ['_avg_stat_by_type_pos', '2'],
   'position-type': ['_avg_stat_by_type_pos', '2'],
   'type-year': ['_avg_stat_by_type_year', '2'],
   'year-type': ['_avg_stat_by_type_year', '2'],
   'position-year': ['_avg_stat_by_year_pos', '2'],
   'year-position': ['_avg_stat_by_year_pos', '2'],
   'sumary': ['_avg_stat_by_type_year_pos', '3']
}

migration_api = {
   'sex': ['sex_2016', '1'],
   'year': ['year_sum', '1'],
   'english': ['english_2016', ''],
   'English': ['english_2016', '']
}

twitter_hp_api = {
   'year': ['year', '1'],
   'polarity': ['polarity', '1'],
   'subjectivity': ['subjectivity', '1']
}

twitter_covid_api = {
   'language': ['language_count', '1'],
   'polarity': ['polarity_count', '1'],
   'subjectivity': ['subjectivity_count', '1']
}

