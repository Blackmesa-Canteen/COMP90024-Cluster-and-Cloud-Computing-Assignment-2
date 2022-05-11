# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     database
   Description :  save aurin data to the database
   Author :       Bocan Yang
   date:          01/05/2022
-------------------------------------------------
"""
import couchdb

from config import config as cfg

couch = couchdb.Server(cfg.LOCAL_DB)

def save_common(db_name, data):
    # update new data
    if db_name in couch:
        db = couch[db_name]
        print("db has been created...")
        # return False
    else:
        db = couch.create(db_name)
    
    for doc in data.values():
        try:
            db.save(doc)
        except Exception:
            print("Error saving")
            return False
    return True