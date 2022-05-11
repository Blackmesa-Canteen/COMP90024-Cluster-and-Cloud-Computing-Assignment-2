# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     main
   Description :  main entrance of the aurin
   Author :       Xiaotian Li, Bocan Yang
   date:          14/04/2022
-------------------------------------------------
"""
import json
import csv
import os

from uuid import uuid4

from helper import path, database
from config import config as cfg


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


# save one file data to database
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


# save house price data
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


# save income data
def save_income():
   income_path = path.get_path() + cfg.INCOME_PATH
   data_to_saved = {}
   for file_name in os.listdir(income_path):
      if file_name[-4:] != '.csv': continue
      save_single_file(income_path+file_name, cfg.INCOME_INFO, data_to_saved)

   return database.save_common(cfg.INCOME_DB, data_to_saved)


# save birth data for languages scenario
def save_birth():
   birth_path =  path.get_path() + cfg.BIRTH_PATH
   data_to_saved = save_single_file(birth_path, cfg.BIRTH_INFO, {})
   return database.save_common(cfg.MIGRATION_DB, data_to_saved)


# save born data for languages scenario
def save_born():
   born_path = path.get_path() + cfg.BORN_PATH
   data_to_saved = save_single_file(born_path, cfg.BORN_INFO, {})
   return database.save_common(cfg.MIGRATION_DB, data_to_saved)


# save migration data for languages scenario
def save_migrations():
   migration_path = path.get_path() + cfg.MIGRATION_PATH
   data_to_saved = {}
   for file_name in os.listdir(migration_path):
      if file_name[-4:] != '.csv' or file_name[:4] == 'born': continue
      save_single_file(migration_path+file_name, cfg.MIGRATION_INFO, data_to_saved)
   return database.save_common(cfg.MIGRATION_DB, data_to_saved)

def save_employment():
   employment_path = path.get_path() + cfg.EMPLOYMENT_PATH
   data_to_saved = save_single_file(employment_path, cfg.EMPLOYMENT_INFO, {})
   return database.save_common(cfg.EMPLOYMENT_DB, data_to_saved)

def save_unemployment():
   unemployment_path = path.get_path() + cfg.UNEMPLOYMENT_PATH
   data_to_saved = save_single_file(unemployment_path, cfg.UNEMPLOYMENT_INFO, {})
   return database.save_common(cfg.EMPLOYMENT_DB, data_to_saved)

def save_unemployment_rate():
   unemployment_s_path = path.get_path() + cfg.UNEMPLOYMENT_RATE_PATH
   data_to_saved = save_single_file(unemployment_s_path, cfg.UNEMPLOYMENT_RATE_INFO, {})
   return database.save_common(cfg.EMPLOYMENT_DB, data_to_saved)


# run all the functions to save all data to database
if __name__ == '__main__':
   print(save_house_price())
   print(save_income())
   print(save_born())
   print(save_migrations())
   print(save_birth())
   print(save_employment())
   print(save_unemployment())
   print(save_unemployment_rate())
   pass
