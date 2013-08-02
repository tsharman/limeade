import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options

from urls import url_patterns
from settings import *



class App(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self,url_patterns, **settings)

#application = App()

application = tornado.web.Application(url_patterns, debug=True, **settings)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
    
