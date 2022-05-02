# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     demo_restful_controller
   Description :  TODO
   Author :       Xiaotian Li
   date：          14/04/2022
-------------------------------------------------
"""
from service.database import Database
# import service.design_doc as doc 
from flask import Flask, Blueprint, abort, jsonify, request

twitter_controller = Blueprint('twitter_controller', __name__)
server = Database()

books = []


@twitter_controller.route('/house-price', methods=['GET'])
def get_house_price():
    server.connect()
    return server.get_twitter_house_price()

@twitter_controller.route('/house-price/<view>', methods=['GET'])
def get_house_with_view(view):
    server.connect()
    return server.get_twitter_house_price(view)

@twitter_controller.route('/house-price/<view>/<statistics>', methods=['GET'])
def get_house_price_with_statistics(view, statistics):
    server.connect()
    return server.get_twitter_house_price(view, statistics)


@twitter_controller.route('/covid', methods=['GET'])
def get_covid():
    server.connect()
    return server.get_twitter_covid()

@twitter_controller.route('/covid/<view>', methods=['GET'])
def get_covid_with_view(view):
    server.connect()
    return server.get_twitter_covid(view)

@twitter_controller.route('/covid/<view>/<statistics>', methods=['GET'])
def get_covid_with_statistics(view, statistics):
    server.connect()
    return server.get_twitter_covid(view, statistics)






@twitter_controller.route('/book/', methods=['GET'])
def get_books():
    return jsonify({'books': books})


@twitter_controller.route('/book/<int:id>', methods=['GET'])
def get_book_by_id(id):  # put application's code here
    for book in books:
        if book['id'] == id:
            return jsonify({'book': book})
    abort(404)


@twitter_controller.route('/book/', methods=['POST'])
def create_book():
    if not request.form or not 'title' in request.form:
        abort(400)
    book = {
        'id': books[-1]['id'] + 1,
        'title': request.form['title'],
        'author': request.form['author'],
        'price': request.form['price'],
    }
    books.append(book)
    return jsonify({'book': book}), 201


@twitter_controller.route('/book/<int:id>', methods=['PUT'])
def update_book_by_id(id):
    for book in books:
        if book['id'] == id:
            book["title"] = request.form['title']
            book["author"] = request.form['author']
            book["price"] = request.form['price']
        return jsonify({'books': books})
    abort(400)


@twitter_controller.route('/book/<int:id>', methods=['DELETE'])
def delete_book_by_id(id):
    for book in books:
        if book['id'] == id:
            books.remove(book)
            return jsonify({'result': True})
    abort(404)

    return jsonify({'result': True})
