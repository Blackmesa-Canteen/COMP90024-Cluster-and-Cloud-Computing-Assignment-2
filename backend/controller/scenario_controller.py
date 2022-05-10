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


# Get languages data with month level for display
@scenario_controller.route('/house-price', methods=['GET'])
def process_house_price():
    server.connect()

    results = server.get_house_price()
    result = results['rows']
    data1 = {
        'name': 'aurin',
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

    results_t1 = server.get_twitter_house_price('map-sum')
    results_t2 = server.get_twitter_house_price('map-count')

    result = results_t1['rows']
    res_length = len(result)

    data2 = {
        'name':'twitter',
        'details': {}
    }

    for i in range(res_length):
        time_t = result[i]['key'][0]
        pos = result[i]['key'][1]
        pola_sum = result[i]['value']
        pola_cnt = results_t2['rows'][i]['value']
        pola_avg = round((pola_sum/pola_cnt), 4)
        if time_t not in data2['details']:
            data2['details'][time_t] = {
                pos: pola_avg
            }
        else:
            data2['details'][time_t][pos] = pola_avg
    
    data = [data1, data2]

    return jsonify(data)