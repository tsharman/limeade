import tornado.web
import tornado.auth
from db import *
import json
from bson import json_util
from bson.objectid import ObjectId

class HomeHandler(tornado.web.RequestHandler):
    def get(self, collection_id=None): 
        database = db_client()
        if collection_id != None:
            video = database.videos.find_one({"_id" : ObjectId(collection_id)})
            blogs = database.blogs.find()
            self.render("home.html", video=video, blogs=blogs)
        else:
            blogs = database.blogs.find()
            self.render("home.html", video=None, blogs=blogs)

class SignUpHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("home.html")


class TwitterLoginHandler(tornado.web.RequestHandler, tornado.auth.TwitterMixin):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        if self.get_argument("oauth_token", None):
            user = yield self.get_authenticated_user()
        else:
            yield self.authorize_redirect()
