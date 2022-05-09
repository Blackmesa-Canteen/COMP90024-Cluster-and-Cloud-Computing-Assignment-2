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