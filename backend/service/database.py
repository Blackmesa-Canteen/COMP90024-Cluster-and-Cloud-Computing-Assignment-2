from util import config_handler as cfg_handler
from util import constants
import requests
import couchdb
import json

class Database:

    def __init__(self):
        cfg = cfg_handler.ConfigHandler()
        self.db_hosts = cfg.get_db_host_list()
        self.db_port = cfg.get_db_port()
        self.db_username = cfg.get_db_username()
        self.db_password = cfg.get_db_password()

        # tmp
        self.master_host = self.db_hosts[0] + ':' + cfg.get_db_port()
        self.req_url = self.get_server_link() + '/{db}/_design/{doc}/_view/{view_name}{group_level}'
        
    def get_server_link(self):
        server_link = 'http://'+ self.db_username + ':'+ self.db_password + '@' + self.master_host + '/'
        return server_link

    def connect(self):
        self.server = couchdb.Server(self.get_server_link())

    def show_info(self):
        print(self.server.version())

    def get_rai(self):
        req_link = self.req_url.format(db='aurin_rai_db', doc='rai_view', view_name='show_all', group_level='')
        response = requests.get(req_link)
        result = json.loads(response.text)
        return result

    def get_income(self, view=None):
        view_name = 'income'
        group_level = ''
        if view is not None:
            try:
                view_name = constants.income_api[view][0]
                group_level = '?group_level=' + constants.income_api[view][1]
            except KeyError:
                view_name = 'kksk'
        req_link = self.req_url.format(db='aurin_income_db', doc='income', view_name=view_name, group_level=group_level)
        response = requests.get(req_link)
        return json.loads(response.text)
    
    def get_house_price(self, type=None, view=None):
        view_name = 'house_price'
        group_level = ''
        doc = 'house_price_view'
        if view is not None:
            try:
                doc = type + '_price'
                view_name = type + constants.hp_api[view][0]
                group_level = '?group_level=' + constants.hp_api[view][1]
            except KeyError:
                view_name = 'kksk'
        req_link = self.req_url.format(db='aurin_house_price_db', doc=doc, view_name=view_name, group_level=group_level)
        response = requests.get(req_link)
        return json.loads(response.text)
    
    def get_twitter_house_price(self, view=None, statistics=None):
        basic_url = self.get_server_link() +  '/history_house_price_tweet_db/_design/house_price_view/_view/'
        if view is None:
            req_url = basic_url + 'show_all'
        elif statistics is None:
            req_url = basic_url + 'show_'  + view
        else:
            req_url = basic_url + statistics + '_' + view
        response = requests.get(req_url + '?group_level=1')
        return json.loads(response.text)
    
    def get_twitter_covid(self, view=None, statistics=None):
        basic_url = self.get_server_link() + '/covid_search_tweet_mentioned_melb_db/_design/covid_view/_view/'
        if view is None:
            req_url = basic_url + 'show_all'
        elif statistics is None:
            req_url = basic_url + 'show_'  + view
        else:
            req_url = basic_url + statistics + '_' + view
        print(req_url)
        response = requests.get(req_url + '?group_level=1')
        print(response.text)
        return json.loads(response.text)

if __name__ == '__main__':
    db = Database()
    print(db.__dict__)
    db.connect()
    print(db.__dict__)

   

