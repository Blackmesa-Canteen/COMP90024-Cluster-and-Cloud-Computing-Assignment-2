# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     database
   Description :  get data from couchdbs
   Author :       Bocan Yang
   date:          1/05/2022
-------------------------------------------------
"""

from util import config_handler as cfg_handler
from util import constants
from util.simple_db_load_balancer import SimpleDbLoadBalancer as Balancer
import requests
import couchdb
import json

class Database:

    # Constructor
    def __init__(self):
        self.cfg = cfg_handler.ConfigHandler()
        self.db_hosts = self.cfg.get_db_host_list()
        self.db_port = self.cfg.get_db_port()
        self.db_username = self.cfg.get_db_username()
        self.db_password = self.cfg.get_db_password()

        self.master_host = self.db_hosts[0] + ':' + self.cfg.get_db_port()
        self.req_url = self.get_server_link() + '/{db}/_design/{doc}/_view/{view_name}{group_level}'
        

    # Use simple balancer to access a random database
    def get_server_link(self):
        db_balancer = Balancer()
        db_host = db_balancer.get_current_db_host() + ':' + self.db_port
        server_link = 'http://'+ self.db_username + ':'+ self.db_password + '@' + db_host
        return server_link


    # Connect to the database
    def connect(self):
        self.server = couchdb.Server(self.get_server_link())


    # Show Information of the database version
    def show_info(self):
        print(self.server.version())


    # Get aurin income data
    def get_income(self, view=None, db_name='aurin_income_db'):
        # defualt names
        view_name = 'income_year_pos'
        group_level = ''

        if view is not None:
            try:
                view_name = constants.income_api[view][0]
                group_level = '?group_level=' + constants.income_api[view][1]
            except KeyError:
                view_name = 'kksk'
        
        # send request and get response
        req_link = self.req_url.format(db=db_name, doc='scenario', 
            view_name=view_name, group_level=group_level)
        response = requests.get(req_link)

        return json.loads(response.text)
    

    # Get aurin house price data
    def get_house_price(self, type=None, view=None, db_name='aurin_house_price_db'):
        # defualt names
        view_name = 'sale_quarter_pos_type'
        group_level = ''
        
        # send request and get response
        req_link = self.req_url.format(db=db_name, 
            doc='scenario', view_name=view_name, group_level=group_level)
        response = requests.get(req_link)

        return json.loads(response.text)
    
    # Get aurin migration data
    def get_migration(self, view=None, db_name='aurin_migration_db'):
        # defualt names
        view_name = 'year'
        group_level = ''

        if view is not None:
            try:
                view_api = constants.migration_api[view]
                view_name = view_api[0]
                group_level = ('?group_level=' + view_api[1]) if view_api[1] != '' else ''
            except KeyError:
                view_name = 'kksk'
        
        # send request and get response
        req_link = self.req_url.format(db=db_name, 
            doc='scenario', view_name=view_name, group_level=group_level)
        response = requests.get(req_link)

        return json.loads(response.text)
    

    # Get aurin employment data
    def get_employments(self, view, db_name='aurin_employment_db'):
        view_api = constants.employ_api[view]
        view_name = view_api[0]
        group_level = ('?group_level=' + view_api[1])

        req_link = self.req_url.format(db=db_name, 
            doc='scenario', view_name=view_name, group_level=group_level)
        response = requests.get(req_link)

        return json.loads(response.text)


    # Get twitter data about house price 
    def get_twitter_house_price(self, view=None, db_name='history_house_price_tweet_db'):
        # defualt names
        view_name = 'polarity'
        group_level = ''
        db_name = self.cfg.get_hp_db()

        if view is not None:
            try:
                view_name = constants.twitter_hp_api[view][0]
                group_level = '?group_level=' + constants.twitter_hp_api[view][1]
            except KeyError:
                view_name = 'kksk'
        
        req_link = self.req_url.format(db=db_name, doc='scenario',
            view_name=view_name, group_level=group_level)
        response = requests.get(req_link)

        return json.loads(response.text)
    

    # Get twitter data about covid 
    def get_twitter_covid(self, view=None, db=None):
        # defualt names
        view_name = 'show_all'
        group_level = ''
        db_name = self.cfg.get_covid_db() if db is None else db

        if view is not None:
            try:
                view_name = constants.twitter_covid_api[view][0]
                group_level = '?group_level=' + constants.twitter_covid_api[view][1]
            except KeyError:
                view_name = 'kksk'
        
        req_link = self.req_url.format(db=db_name, doc='scenario',
            view_name=view_name, group_level=group_level)
        print(req_link)
        response = requests.get(req_link)

        return json.loads(response.text)
    
    
    # Get languages data from twitter data
    def get_languages(self, db_list, time=None):
        view_name = 'language_count' if time is None else 'language_month_count'
        responses = []

        for db_name in db_list:
            req_link = self.req_url.format(db=db_name, 
                doc='languages', view_name=view_name, group_level='?group_level=3')
            response = requests.get(req_link)
            responses.append(json.loads(response.text))
        
        return responses
    

    # Get live stream tweets or latest 10 tweets ids from database
    def get_live_twitter(self, view):
        db_name = self.cfg.get_stream_db()

        if view != 'latest':
            view_api = constants.twitter_live_api[view]
            view_name = view_api[0]
            group_level = ('?group_level=' + view_api[1])
            req_link = self.req_url.format(db=db_name, 
                doc='scenario', view_name=view_name, group_level=group_level)
        else:
            req_link = self.get_server_link() + '/' + db_name + '/_changes?descending=true&limit=10'
        
        response = requests.get(req_link)
        return json.loads(response.text)
    

    # Get 10 tweets by ids
    def get_tweets(self, ids):
        results = []
        db_name = self.cfg.get_stream_db()
        req_link = self.get_server_link() + '/' + db_name + '/'
        for id in ids:
            each_req = req_link + id
            response = requests.get(each_req)
            results.append(json.loads(response.text))
        return results
    
    
# Test
if __name__ == '__main__':
    db = Database()
    print(db.__dict__)
    db.connect()
    print(db.__dict__)

   

