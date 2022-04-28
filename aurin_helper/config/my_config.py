# test config file
# local development
USERNAME = 'admin'
PASSWORD = 'password'
LOCAL_DB = 'http://'+ USERNAME + ':'+ PASSWORD + '@127.0.0.1:5984/'

# CSV for test, or JSON -> Now CSV
DATA_TYPE = 'CSV'

# rental affordability index data
# RAI_META_PATH = '/data/Aurin/House/sgs_rai_index_gcc_total_2021-metadata-3073435027842782756.json'
RAI_FILE_PATH = '/data/Aurin/House/sgs_rai_index_gcc_total_2021-3301684475030977756.csv'
HOUSE_PRICE_RAI_DB = 'rai_2011_to_2021_db'