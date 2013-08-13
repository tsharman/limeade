from pymongo import MongoClient
import os

if os.environ.get('PROD') == None:
  from local_settings import *
else:
  mongo_db_uri = os.environ.get('MONGO_DB_URI')
  mongo_db_port = int(os.environ.get('MONGO_DB_PORT'))

def db_client():
    client = MongoClient(mongo_db_uri, mongo_db_port)
    print mongo_db_port
    db = client['musicvideo']
    return db


