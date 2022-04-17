# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     config_handler
   Description :  siongleton helper to parse and hold config
   Author :       Xiaotian Li
   date：          14/04/2022
-------------------------------------------------
"""
import os

import yaml

import path_helper


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
            root_path = path_helper.get_project_root_path()
            self.__config_file_path = os.path.join(
                root_path, 'config', 'app_config.yaml')

            print("config file read from: " +
                  self.__config_file_path)

            if not os.path.exists(self.__config_file_path):
                print("config file not exist!")
                exit(-1)

            with open(self.__config_file_path, 'r', encoding='utf-8') as f:
                cfgs = yaml.safe_load(f)
                self.__db_host_list = cfgs['app']['db']['host-list']
                self.__db_port = str(cfgs['app']['db']['port'])
                self.__db_username = str(cfgs['app']['db']['username'])
                self.__db_password = str(cfgs['app']['db']['password'])

                self.__key_word_list = cfgs['app']['key-word-list']
                self.__api_key = cfgs['app']['api-key']
                self.__api_secret = cfgs['app']['api-secret']
                self.__api_token = cfgs['app']['api-token']

                self.__target_db_name = cfgs['app']['target-db-name']
                self.__target_box_point_a = cfgs['app']['target-box-points'][0]
                self.__target_box_point_b = cfgs['app']['target-box-points'][1]
                self.__is_fetch_english_tweet_only = cfgs['app']['is-fetch-english-tweet-only']

                self.__block_queue_size = cfgs['app']['concurrency']['block-queue-size']

        return cls.__instance

    # once we used __new__, __init__ is not needed
    def __init__(self):
        pass

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

    def get_key_word_list(self):
        return self.__key_word_list

    def get_api_key(self):
        return self.__api_key

    def get_api_secret(self):
        return self.__api_secret

    def get_api_token(self):
        return self.__api_token

    def get_target_db_name(self):
        return self.__target_db_name

    def get_target_box_point_a(self):
        return self.__target_box_point_a

    def get_target_box_point_b(self):
        return self.__target_box_point_b

    def is_fetch_english_tweet_only(self):
        return self.__is_fetch_english_tweet_only

    def get_block_queue_size(self):
        return self.__block_queue_size


if __name__ == '__main__':
    config_handler = ConfigHandler()
    print(config_handler.get_db_host_list())
    print(config_handler.get_db_host_port_list())
    print(config_handler.get_db_port())
    print(config_handler.get_db_username())
    print(config_handler.get_db_password())
    print(config_handler.get_key_word_list())

    print(config_handler.get_target_box_point_a()['longtitude'])
    print(config_handler.is_fetch_english_tweet_only())
    print(config_handler.get_block_queue_size())
