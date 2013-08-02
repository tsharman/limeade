from pymongo import MongoClient

print "meow"

if os.environ.get('PROD') == None:
  from local_settings import *
else:
  print "Test"
  mongo_db_uri = os.environ.get('MONGO_DB_URI')
  mongo_db_port = os.environ.get('MONGO_DB_PORT')

def db_client():
    client = MongoClient(mongo_db_uri, mongo_db_port)
    db = client['musicvideo']
    return db


