import tornado.web
from db import *
import json
from bson import json_util

class BlogListHandler(tornado.web.RequestHandler):
    def get(self):
        database = db_client()
        blogs = database.blogs.find().sort( [['_id', -1]])

        return_blogs = []
        for blog in blogs:
            return_blogs.append(blog)


        self.write(json.dumps(return_blogs, default=json_util.default))
