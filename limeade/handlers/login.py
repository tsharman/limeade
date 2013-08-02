import tornado.web
from db import *
import json
from bson import json_util
from bson.objectid import ObjectId

class HomeHandler(tornado.web.RequestHandler):
    def get(self, collection_id=None): 
        if collection_id != None:
            database = db_client()
            video = database.videos.find_one({"_id" : ObjectId(collection_id)})
            self.render("home.html", video=video)
        else:
            self.render("home.html", video=None)

class SignUpHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("home.html")

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("home.html")

