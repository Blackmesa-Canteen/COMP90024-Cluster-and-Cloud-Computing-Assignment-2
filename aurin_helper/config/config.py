# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     config
   Description :  simple static config py file
   Author :       Xiaotian Li
   date：          14/04/2022
-------------------------------------------------
"""

# 因为aurin_helper只是运行一次, 上传数据给数据库就行, 所以就不用负载均衡了
DB_USERNAME = 'admin'
DB_PASSWORD = 'adm$n'
DB_PORT = '5984'
DB_HOST = '321.321.321.321'

# 可能取好几类人文数据, 放入对应的数据库里
DB_EDUCATION_LEVEL_NAME = 'aurin-education-level'
DB_INCOME_NAME = 'aurin-income'