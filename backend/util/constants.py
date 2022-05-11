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


# aurin income APIs
income_api = {
   'position': ['income_pos', '1'],
   'year': ['income_year', '1'],
   'year-position': ['income_year_pos', '2'],
   'position-year': ['income_year_pos', '2']
}

# aurin house price APIs
hp_api = {
   'sumary': ['sale_quarter_pos_type', '3'],
}

# aurin migration APIs
migration_api = {
   'year': ['year_sum', '1'],
   'population': ['population_sum', '1'],
   'total-population': ['total_population_sum', '1'],
}

# aurin employment APIs
employ_api = {
   'unemployment': ['unemployment_sum', '1'],
   'unemployment-rate': ['unemployment_rate_sum', '1'],
   'employment': ['employment_sum', '1']
}

# twitter house price APIs
twitter_hp_api = {
   'language': ['language_count', '1'],
   'language-year': ['language_year_count', '2'],
   'language-quarter': ['language_quarter_count', '3'],
   'language-month': ['language_month_count', '3'],
   'year': ['year_count', '1'],
   'polarity': ['polarity_count', '1'],
   'subjectivity': ['subjectivity_count', '1'],
   'map': ['map_count', '1'],
   'map-avg': ['map_polarity_quarter_avg', '2'],
}

# twitter covid APIs
twitter_covid_api = {
   'language': ['language_count', '1'],
   'language-year': ['language_year_count', '2'],
   'language-quarter': ['language_quarter_count', '3'],
   'language-month': ['language_month_count', '3'],
   'polarity': ['polarity_day_avg', '3'],
   'map': ['map_count', '1'],
   'map-year': ['map_year_count', '2'],
}

# twitter stream APIs
twitter_live_api = {
   'polarity': ['polarity_count', '1'],
   'subjectivity': ['subjectivity_count', '1'],
   'source': ['source_count', '1'],
   'language': ['language_count', '1']
}


# historical data distribution, used to estimate fresh twitter data
as4_name_distribution = {
   "Melbourne - Inner": [8641, 0.43114],
   "Melbourne - Inner East": [1462, 0.07295],
   "Melbourne - Inner South": [1657, 0.08268],
   "Melbourne - North East": [2218, 0.11067],
   "Melbourne - North West": [1234, 0.06157],
   "Melbourne - Outer East": [1658, 0.08273],
   "Melbourne - South East": [1490, 0.07434],
   "Melbourne - West": [1564, 0.07804],
   "Mornington Peninsula": [46, 0.0023],
   "Other Place": [72, 0.00359],
}

sorted_random_num = [0.43114, 0.11067, 0.08273, 0.08268, 0.07804, 0.07434, 0.07295, 0.06157, 0.00359, 0.0023]

as4_code_distribution = {
   "206": [8641, 0.43114],
   "207": [1462, 0.07295],
   "208": [1657, 0.08268],
   "209": [2218, 0.11067],
   "210": [1234, 0.06157],
   "211": [1658, 0.08273],
   "212": [1490, 0.07434],
   "213": [1564, 0.07804],
   "214": [46, 0.0023],
   "-1": [72, 0.00359],
}

as4_name_box = {
   "Melbourne - Inner": [144.8890,-37.8910,145.0450,-37.7340],
   "Melbourne - Inner East": [144.9993,-37.8759,145.1841,-37.7340],
   "Melbourne - Inner South": [144.9850,-38.0850,145.1560,-37.8370],
   "Melbourne - North East": [144.8810,-37.7840,145.5800,-37.2630],
   "Melbourne - North West": [144.4593,-37.7730,144.9853,-37.1751],
   "Melbourne - Outer East": [145.1569,-37.9747,145.8784,-37.5266],
   "Melbourne - South East": [145.0800,-38.3320,145.7650,-37.8530],
   "Melbourne - West": [144.3340,-38.0040,144.9160,-37.5460],
   "Mornington Peninsula": [144.6520,-38.5030,145.2620,-38.0670]
}

as4_code_box = {
   "206": [144.8889,-37.8917,145.0453,-37.7325],
   "207": [144.9993,-37.8759,145.1841,-37.7339],
   "208": [144.9834,-38.0850,145.1563,-37.8374],
   "209": [144.8807,-37.7851,145.5800,-37.2629],
   "210": [144.4577,-37.7761,144.9853,-37.1751],
   "211": [145.1569,-37.9750,145.8784,-37.5260],
   "212": [145.0795,-38.3325,145.7651,-37.8533],
   "213": [144.3336,-38.0046,144.9165,-37.5464],
   "214": [144.6514,-38.5030,145.2617,-38.0674]
}