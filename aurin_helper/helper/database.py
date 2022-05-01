import couchdb

from config import my_config as cfg

couch = couchdb.Server(cfg.LOCAL_DB)

def save_rai(data):
    db_name = cfg.HOUSE_PRICE_RAI_DB
    if db_name in couch:
        db = couch[db_name]
        print("db has been created...")
        # return False
    else:
        db = couch.create(db_name)
    for key, value in data.items():
        doc = {'year':key, 'rai': value}
        try:
            db.save(doc)
        except Exception:
            print("Error saving")
            return False
    return True

def save_common(db_name, data):
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