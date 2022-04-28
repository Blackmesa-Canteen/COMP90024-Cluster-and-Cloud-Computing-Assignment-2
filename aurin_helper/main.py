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

from helper import path, database
from config import my_config as cfg

USELESS_INFO = ['geography_name','unique_id', 'state', 'city']

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

def save_rai():
   root_path = path.get_path()   
   file_path = root_path + cfg.RAI_FILE_PATH

   with open(file_path, 'r') as file:
      reader = csv.DictReader(file)
      cnt = 0

      data_to_saved = {}
      for row in reader:
         for key, value in row.items():        
            if key in USELESS_INFO:
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

if __name__ == '__main__':
    # aurin_helper是个初始化用的脚本, 只运行一次
    # 从AURIN网站下载所需的JSON文件到data里
    # 解析JSON, 整理数据后, 上传到数据库
    # 除非数据库内容丢失, 否则不用再运行
    save_rai()
    pass
