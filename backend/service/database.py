from util import config_handler as cfg_handler
from util import constants
from util.simple_db_load_balancer import SimpleDbLoadBalancer as Balancer
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
        db_balancer = Balancer()
        db_host = db_balancer.get_current_db_host() + ':' + self.db_port
        server_link = 'http://'+ self.db_username + ':'+ self.db_password + '@' + db_host
        return server_link

    def connect(self):
        self.server = couchdb.Server(self.get_server_link())

    def show_info(self):
        print(self.server.version())

    def get_rai(self):
        req_link = self.req_url.format(db='aurin_rai_db', doc='rai_view', 
            view_name='show_all', group_level='')
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
        req_link = self.req_url.format(db='aurin_income_db', doc='income', 
            view_name=view_name, group_level=group_level)
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
        req_link = self.req_url.format(db='aurin_house_price_db', 
            doc=doc, view_name=view_name, group_level=group_level)
        response = requests.get(req_link)
        return json.loads(response.text)
    

    def get_twitter_house_price(self, view=None):
        view_name = 'house_price'
        group_level = ''
        if view is not None:
            try:
                view_name = constants.twitter_hp_api[view][0]
                group_level = '?group_level=' + constants.twitter_hp_api[view][1]
            except KeyError:
                view_name = 'kksk'
        req_link = self.req_url.format(db='history_house_price_tweet_db', 
            doc='house_price_view', view_name=view_name, group_level=group_level)
        response = requests.get(req_link)
        return json.loads(response.text)
    

    def get_twitter_covid(self, view=None):
        view_name = 'show_all'
        group_level = ''
        if view is not None:
            try:
                view_name = constants.twitter_covid_api[view][0]
                group_level = '?group_level=' + constants.twitter_covid_api[view][1]
            except KeyError:
                view_name = 'kksk'
        req_link = self.req_url.format(db='covid_search_tweet_mentioned_melb_db', 
            doc='covid', view_name=view_name, group_level=group_level)
        response = requests.get(req_link)
        return json.loads(response.text)
    
    def get_migration(self, view=None):
        view_name = 'show_all'
        group_level = ''
        if view is not None:
            try:
                view_api = constants.migration_api[view]
                view_name = view_api[0]
                group_level = ('?group_level=' + view_api[1]) if view_api[1] != '' else ''
            except KeyError:
                view_name = 'kksk'
        req_link = self.req_url.format(db='aurin_migration_db', 
            doc='migration', view_name=view_name, group_level=group_level)
        response = requests.get(req_link)
        return json.loads(response.text)
    
    def get_languages(self, db_list):
        view_name = 'language_count'
        responses = []
        for db_name in db_list:
            req_link = self.req_url.format(db=db_name, 
                doc='scenario', view_name=view_name, group_level='?group_level=1')
            response = requests.get(req_link)
            responses.append(json.loads(response.text))
        return responses

if __name__ == '__main__':
    db = Database()
    print(db.__dict__)
    db.connect()
    print(db.__dict__)
    res = db.get_migration('population')
    print(res)

   

