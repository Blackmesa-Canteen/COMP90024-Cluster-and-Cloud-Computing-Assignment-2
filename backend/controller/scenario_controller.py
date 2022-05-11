# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     scenario_controller
   Description :  Controller for scenarios API handling
   Author:        Xiaotian Li, Bocan Yang
   Date:          14/04/2022
-------------------------------------------------
"""
from service.database import Database
from util import constants
from flask import Blueprint, abort, jsonify

scenario_controller = Blueprint('scenario_controller', __name__)
server = Database()

# Get languages data
@scenario_controller.route('/languages', methods=['GET'])
def process_languages():
    server.connect()

    # Get Twitter language counting information
    processed_dbs = constants.language_db_names
    twitter_results = server.get_languages(processed_dbs)
    twitter_data = {
        'name': 'twitter',
        'total': 0,
        'details': {}
    }
    for result in twitter_results:
        languages = result['rows']
        for language in languages:
            twitter_data['total'] += language['value']
            if (lang:= language['key']) not in twitter_data['details']:
                twitter_data['details'][lang] = language['value']
            else:
                twitter_data['details'][lang] += language['value']
    twitter_data['english_proportion'] = twitter_data['details']['en'] / twitter_data['total']

    # Get 2016 Population (foreigner) base data
    population_result = server.get_migration('population')['rows'][0]
    population = {
        'name': 'population',
        'details': {}
    }
    population['details'][population_result['key']] = population_result['value']

    # Get 2017 - 2020 Population Migration Data
    migration = {
        'name': 'migration',
        'details': {}
    }
    migration_results = server.get_migration('year')['rows']
    for result in migration_results:
        year = result['key']
        year_int = int(year)
        num = result['value']
        migration['details'][year] = num
        population['details'][year] = population['details'][str(year_int-1)] + num
    
    # Get 2016 - 2020 Total Population Data
    total_population = {
        'name': 'total_population',
        'details': {}
    }
    total_results = server.get_migration('total-population')['rows']
    for result in total_results:
        year = result['key']
        num = result['value']
        total_population['details'][year] = num

    data = [twitter_data, migration, population, total_population]

    return jsonify(data)


# Get languages data with month level for display
@scenario_controller.route('/languages-month', methods=['GET'])
def process_languages_with_time():
    server.connect()

    # Get Twitter language counting information
    processed_dbs = constants.language_db_names
    results = server.get_languages(processed_dbs, "month")
    data = {}
    for result in results:
        for each in result['rows']:
            month = each['key'][0] + '-' + each['key'][1]
            lang = each['key'][2]
            count = each['value']
            if month not in data:
                data[month] = {lang: count}
            else:
                data[month][lang] = count
    return jsonify(data)


# Get house price data for display
@scenario_controller.route('/house-price', methods=['GET'])
def process_house_price():
    server.connect()

    results = server.get_house_price()
    result = results['rows']
    data1 = {
        'name': 'aurin_house_price',
        'details': {}
    }
    for each in result:
        key = each['key']
        value = each['value']
        _time = key[0] + '-' + key[1]
        pos_price = {
            key[2]: {
                'avg': value[0],
                'max': value[1]
            }
        }
        _type = key[3]
        if _time not in data1['details']: 
            data1['details'][_time] = {
                _type: pos_price
            }
        else:
            if _type not in data1['details'][_time]:
                data1['details'][_time][_type] = pos_price
            else:
                data1['details'][_time][_type][key[2]] = {
                    'avg': value[0],
                    'max': value[1]
                }

    data2 = {
        'name': 'aurin_income',
        'details': {}
    }
    results_income = server.get_income('year-position')['rows']
    for res in results_income:
        time = res['key'][0]
        position = res['key'][1]
        if time not in data2['details']:
            data2['details'][time] = {position: res['value']}
        else:
            data2['details'][time][position] = res['value']

    results_twitter = server.get_twitter_house_price('map-avg')['rows']

    print(results_twitter)

    data3 = {
        'name':'twitter',
        'details': {}
    }

    for res in results_twitter:
        time = res['key'][0]
        position = res['key'][1]
        polarity = round(res['value'], 4)
        if time not in data3['details']:
            data3['details'][time] = {position: polarity}
        else:
            data3['details'][time][position] = polarity

    data = [data1, data2, data3]

    return jsonify(data)

@scenario_controller.route('/covid', methods=['GET'])
def process_covid():
    server.connect()

    unempoly_results = server.get_employments("unemployment")['rows']
    unempoly_rate_results = server.get_employments("unemployment-rate")['rows']
    empoly_results = server.get_employments("employment")['rows']

    data1 = {
        'name': 'unemployment',
        'details': {}
    }

    for res in unempoly_results:
        time = res['key'][-7:]
        data1['details'][time] = res['value']
    
    data2 = {
        'name': 'unemployment_rate',
        'details': {}
    }

    for res in unempoly_rate_results:
        time = res['key'][-7:]
        data2['details'][time] = res['value']
    
    data3 = {
        'name': 'unemployment',
        'details': {}
    }

    for res in empoly_results:
        time = res['key'][-7:]
        data3['details'][time] = res['value']

    data4 = {
        'name': 'total_polarity',
        'details': {}
    }
    total_results = server.get_twitter_covid('polarity')['rows']
    for res in total_results:
        key = res['key']
        time = key[0] + '-' + key[1]
        data4['details'][time] = round(res['value'], 4)

    data5 = {
        'name': 'lockdowm_polarity',
        'details': {}
    }
    lockdown_results = server.get_twitter_covid('polarity', 
        'covid_search_tweet_melb_jul_to_sep_2020_db')['rows']
    for res in lockdown_results:
        key = res['key']
        time = key[0] + '-' + key[1] + '-' + key[2]
        data5['details'][time] = round(res['value'], 4)

    data = [data1, data2, data3, data4, data5]
    return jsonify(data)



@scenario_controller.route('/stream', methods=['GET'])
def process_live_twitter():
    server.connect()

    results_p = server.get_live_twitter('polarity')['rows']
    results_s = server.get_live_twitter('subjectivity')['rows']
    results_src = server.get_live_twitter('source')['rows']
    latest_tweets = server.get_live_twitter('latest')

    data1 = {
        'name': 'polarity',
        'details': {}
    }

    for res in results_p:
        data1['details'][res['key']] = res['value']
    
    data2 = {
        'name': 'subjectivity',
        'details': {}
    }

    for res in results_s:
        data2['details'][res['key']] = res['value']

    data3 = {
        'name': 'source',
        'details': {}
    }

    for res in results_src:
        data3['details'][res['key']] = res['value']
    

    data4 = {
        'name': 'smaple',
        'details': []
    }

    ids = []
    for res in latest_tweets['results']:
        ids.append(res['id'])
    
    tweets = server.get_tweets(ids)
    for tweet in tweets:
        print(tweet)
        try:
            data4['details'].append({
                'time': tweet['created_at'],
                'lang': tweet['lang'],
                'source': tweet['source'],
                'text': tweet['text'],
                'polarity': tweet['polarity'],
                'subjectivity': tweet['subjectivity']
            })
        except KeyError:
            continue

    data = [data1, data2, data3, data4]
    return jsonify(data)
