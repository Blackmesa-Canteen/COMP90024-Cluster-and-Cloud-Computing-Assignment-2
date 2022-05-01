# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     main
   Description :  main entrance of the aurin
   Author :       Xiaotian Li
   date：          14/04/2022
-------------------------------------------------
"""
import json
import csv
import os

from uuid import uuid4

from helper import path, database
from config import my_config as cfg


# transform E price (1.222E8) to float value
def process_price(val):
   if 'E' in val:
      try:
         a = float(val.split('E')[0])
         b = float(val.split('E')[1])
         price = str(a * (10 ** b))
      except ValueError:
         return val
   else:
      price = val
   return price


# process rai data format
def process_data(data):
   saved_data = {}
   for key, val in data.items():
      year_quarter = key[-7:].split('_')
      year, quarter = year_quarter[0], year_quarter[1]
      avg_q = val['sum'] / val['count']
      if year not in saved_data:
         saved_data[year] = {'total': avg_q, 'quarters': {}}
      else:
         saved_data[year]['total'] += avg_q
      saved_data[year]['quarters'][quarter] = avg_q
   return saved_data


def save_single_file(file_path, data_info, data_to_saved):
   with open(file_path, 'r') as file:
      reader = csv.DictReader(file)
      for row in reader:
         row_data = {}
         for key, value in row.items():
            if (key:= key.strip()) in data_info.keys():
               row_data[data_info[key]] = value
         data_to_saved[uuid4().hex] = row_data
   return data_to_saved


def save_rai(): 
   file_path = path.get_path() + cfg.RAI_FILE_PATH

   with open(file_path, 'r') as file:
      reader = csv.DictReader(file)
      data_to_saved = {}

      for row in reader:
         for key, value in row.items():        
            if key in cfg.USELESS_INFO:
               continue # skip
            value = float(value) if value != 'null' else 0.0
            if key not in data_to_saved:
               data_to_saved[key] = {
                  'sum': value,
                  'count': 1 if value != 0.0 else 0
               }
            else:
               data_to_saved[key]['sum'] += value
               data_to_saved[key]['count'] += 1 if value != 0.0 else 0

      saved_data = process_data(data_to_saved)
      return database.save_rai(saved_data)


def save_house_price():
   hp_root_path = path.get_path() + cfg.HOUSE_PRICE_PATH
   file_paths = list(map(lambda year: hp_root_path+year, cfg.HOUSE_PRICE_TIME))
   data_to_saved = {}

   for file_path in file_paths:
      for file_name in os.listdir(file_path):
         if file_name[-4:] != '.csv': continue
         with open(file_path+file_name, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
               row_data = {}
               for key, value in row.items():
                  if (key:= key.strip()) in cfg.HOUSE_PRICE_INFO.keys():
                     row_data[cfg.HOUSE_PRICE_INFO[key]] = process_price(value)
               data_to_saved[uuid4().hex] = row_data

   return database.save_common(cfg.HOUSE_PRICE_DB, data_to_saved)


def save_income():
   income_path = path.get_path() + cfg.INCOME_PATH
   data_to_saved = {}
   for file_name in os.listdir(income_path):
      if file_name[-4:] != '.csv': continue
      save_single_file(income_path+file_name, cfg.INCOME_INFO, data_to_saved)

   return database.save_common(cfg.INCOME_DB, data_to_saved)


def save_born():
   born_path = path.get_path() + cfg.BORN_PATH
   data_to_saved = save_single_file(born_path, cfg.BORN_INFO, {})
   return database.save_common(cfg.MIGRATION_DB, data_to_saved)


def save_migrations():
   migration_path = path.get_path() + cfg.MIGRATION_PATH
   data_to_saved = {}
   for file_name in os.listdir(migration_path):
      if file_name[-4:] != '.csv' or file_name[:4] == 'born': continue
      save_single_file(migration_path+file_name, cfg.MIGRATION_INFO, data_to_saved)
   return database.save_common(cfg.MIGRATION_DB, data_to_saved)


def save_education():
   education_path = path.get_path() + cfg.EDUCATION_PATH
   data_to_saved = {}
   for file_name in os.listdir(education_path):
      if file_name[-4:] != '.csv': continue
      save_single_file(education_path+file_name, cfg.EDUCATION_INFO, data_to_saved)
   return database.save_common(cfg.EDUCATION_DB, data_to_saved)


if __name__ == '__main__':
   # aurin_helper是个初始化用的脚本, 只运行一次
   # 从AURIN网站下载所需的JSON文件到data里
   # 解析JSON, 整理数据后, 上传到数据库
   # 除非数据库内容丢失, 否则不用再运行
   # print(save_rai())
   # print(save_house_price())
   # print(save_income())
   # print(save_born())
   # print(save_migrations())
   # print(save_education())
   
   pass
