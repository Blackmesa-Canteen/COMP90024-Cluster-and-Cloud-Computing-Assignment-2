# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     demo_controller
   Description :  TODO
   Author :       Xiaotian Li
   date:          14/04/2022
-------------------------------------------------
"""
from flask import Flask, Blueprint

demo_controller = Blueprint('demo_controller', __name__)

@demo_controller.route('/')
def show_demo_msg():  # put application's code here
    return 'Hello World!'
