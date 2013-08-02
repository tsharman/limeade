from pymongo import MongoClient
from local_settings import *
def db_client():
    client = MongoClient(mongo_db_uri, mongo_db_port)
    db = client['musicvideo']
    return db


