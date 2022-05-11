# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     config_handler
   Description :  siongleton helper to parse and hold config
   Author :       Xiaotian Li, Bocan Yang
   date:          14/04/2022
-------------------------------------------------
"""
import os
from time import sleep

import yaml

import path_helper as path


class ConfigHandler:
    # singleton
    __instance = None

    # singleton
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(ConfigHandler, cls).__new__(
                cls, *args, **kwargs)

            # init
            self = cls.__instance
            root_path = path.get_project_root_path()
            self.__config_file_path = os.path.join(
                root_path, 'config', 'app_config.yaml')

            print("config file read from: " +
                        self.__config_file_path)

            if not os.path.exists(self.__config_file_path):
                print("config file not exist!")
                exit(-1)

            with open(self.__config_file_path, 'r', encoding='utf-8') as f:
                cfgs = yaml.safe_load(f)
                self.__db_master_node = cfgs['app']['db']['master-node']
                self.__db_host_list = cfgs['app']['db']['host-list']
                self.__db_port = str(cfgs['app']['db']['port'])
                self.__db_username = cfgs['app']['db']['username']
                self.__db_password = cfgs['app']['db']['password']
                self.__hp_db = cfgs['app']['db']['house-price-db']
                self.__covid_db = cfgs['app']['db']['covid-db']
                self.__lockdown_db = cfgs['app']['db']['lockdown-db']
                self.__stream_db = cfgs['app']['db']['stream-db']

        return cls.__instance

    # once we used __new__, __init__ is not needed
    def __init__(self):
        pass

    def get_hp_db(self):
        return self.__hp_db
    
    def get_covid_db(self):
        return self.__covid_db
    
    def get_lockdown_db(self):
        return self.__lockdown_db
    
    def get_stream_db(self):
        return self.__stream_db
    
    def get_covid_dbs(self):
        return [self.__covid_db, self.__lockdown_db]

    def get_twitter_dbs(self):
        return [self.__hp_db, self.__covid_db, self.__lockdown_db, self.__stream_db]
    
    def get_db_master_node(self):
        return self.__db_master_node

    def get_db_host_list(self):
        """
        :return: list of hosts: ["123.123.123.123", "233.2332.332.233"]

        author Xiaotian Li
        """

        return self.__db_host_list

    def get_db_port(self):
        return self.__db_port

    def get_db_username(self):
        return self.__db_username

    def get_db_password(self):
        return self.__db_password

    def get_db_host_port_list(self):
        """
        :return: list of hosts with port: ["123.123.123.123:5984", "233.2332.332.233:5984"]

        author Xiaotian Li
        """

        res = []
        for host in self.__db_host_list:
            res.append(host + ':' + self.__db_port)

        return res

if __name__ == '__main__':
    cfg = ConfigHandler()
    # print(config_handler.get_db_host_list())
    # print(cfg.get_covid_db())
    # print(cfg.get_hp_db())
    # print(cfg.get_lockdown_db())
    # print(cfg.get_stream_db())
    print(cfg.get_covid_dbs())
    print(cfg.get_twitter_dbs())