# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     simple_load_balancer
   Description :  thread-safe load balancer to RR the request host of couch DB
   Author :       Xiaotian Li
   date：          14/04/2022
-------------------------------------------------
"""
import threading


from loguru import logger

from common_util.config_handler import ConfigHandler


class SimpleDbLoadBalancer:
    # singleton
    __instance = None

    # singleton
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(SimpleDbLoadBalancer, cls).__new__(
                cls, *args, **kwargs)

            # init
            self = cls.__instance

            self.__index = 0

            config_handler = ConfigHandler()
            # self.__host_list = config_handler.get_db_host_list()
            self.__host_list = config_handler.get_db_host_port_list()
            self.__host_list_size = len(self.__host_list)

            self.lock = threading.RLock()

        return cls.__instance

    # once we used __new__, __init__ is not needed
    def __init__(self):
        pass

    def get_current_db_host(self):
        """
        Round-Robin to get a host
        :return:
        """
        self.lock.acquire()
        try:
            if self.__index < self.__host_list_size:
                res = self.__host_list[self.__index]

                # prevent over bound
                if self.__index < self.__host_list_size - 1:
                    self.__index += 1
                else:
                    self.__index = 0

                return res
            else:
                logger.error("host list out of bound at get_current_db_host")
                exit(-1)
        finally:
            self.lock.release()


if __name__ == '__main__':
    balancer = SimpleDbLoadBalancer()
    print(balancer.get_current_db_host())
    print(balancer.get_current_db_host())
    print(balancer.get_current_db_host())
    print(balancer.get_current_db_host())
    print(balancer.get_current_db_host())
    print(balancer.get_current_db_host())
    print(balancer.get_current_db_host())
    print(balancer.get_current_db_host())
    print(balancer.get_current_db_host())
    print(balancer.get_current_db_host())
