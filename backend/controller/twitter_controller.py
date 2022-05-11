# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     twitter_controller
   Description :  Controller for twitter API handling
   Author:        Xiaotian Li, Bocan Yang
   Date:          14/04/2022
-------------------------------------------------
"""
from service.database import Database
from flask import Blueprint, abort, jsonify

twitter_controller = Blueprint('twitter_controller', __name__)
server = Database()

# Get all house price data
@twitter_controller.route('/house-price', methods=['GET'])
def get_house_price():
    server.connect()
    return server.get_twitter_house_price()

# Get specific view of house price data
@twitter_controller.route('/house-price/<view>', methods=['GET'])
def get_house_price_with_view(view):
    server.connect()
    result = server.get_twitter_house_price(view)
    try:
        data = result['rows']
    except KeyError:
        abort(404)
    print(data)
    return jsonify(data)


# Get all covid data
@twitter_controller.route('/covid', methods=['GET'])
def get_covid():
    server.connect()
    return server.get_twitter_covid()

# Get specific view of data
@twitter_controller.route('/covid/<view>', methods=['GET'])
def get_covid_with_view(view):
    server.connect()
    result = server.get_twitter_covid(view)
    try:
        data = result['rows']
    except KeyError:
        abort(404)
    print(data)
    return jsonify(data)
