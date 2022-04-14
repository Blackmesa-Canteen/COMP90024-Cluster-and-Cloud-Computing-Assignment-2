# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     path_helper
   Description :  helper to get root path. DO NOT MOVE THIS FILE.
   Author :       Xiaotian Li
   date：          4/04/2022
-------------------------------------------------
"""
import os

# DO NOT MOVE THIS FILE


def get_project_root_path():
    """
    static method for get root path of the project

    usage: path_helper.get_project_root_path()

    :return: e.g. 'E:\\projects\\SWEN90013-Data-Platform-for-Biomaterial-Testing'

    author: Xiaotian Li
    """
    return os.path.join(
        os.path.dirname(__file__),
    )
