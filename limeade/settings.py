import tornado
import tornado.template
import os

path = lambda root,*a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.abspath(__file__))

MEDIA_ROOT = path(ROOT, 'media')
TEMPLATE_ROOT = path(ROOT, 'templates')

settings = {}
settings['static_path'] = os.path.join(ROOT, 'static')
settings['xsrf_cookies'] = True
settings['template_loader'] = tornado.template.Loader(TEMPLATE_ROOT)

from local_settings import *
settings['twitter_consumer_key'] = twitter_consumer_key
settings['twitter_consumer_secret'] = twitter_consumer_secret
