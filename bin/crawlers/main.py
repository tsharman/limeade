#!/var/www/musicvideo/env/bin/python

from crawler import crawler

# importing all crawling scripts
"""
from sparkups import sparkups_crawler
from gorillavsbear import gorillavsbear_crawler
from portals import portals_crawler
from yvynyl import yvynyl_crawler
from disconaivete import disco_naivete_crawler
from iguessimfloating import iguessimfloating_crawler
from lostlostlost import lostlostlost_crawler
from sonicmasala import sonicmasala_crawler
from stadiumsandshrines import stadiumsandshrines_crawler
from blogotheque import blogotheque_crawler
from smokedontsmoke import smoke_dont_smoke_crawler

# calling all crawling scripts

sparkups_crawler()
gorillavsbear_crawler()
portals_crawler()
yvynyl_crawler()
disco_naivete_crawler()
iguessimfloating_crawler()
lostlostlost_crawler()
sonicmasala_crawler()
stadiumsandshrines_crawler()
blogotheque_crawler()
smoke_dont_smoke_crawler()

"""

blog_urls = [
    "http://www.blogotheque.net/feed/",
    "http://www.gorillavsbear.net/feed/",
    "http://disconaivete.com/rss",
    "http://www.lostlostlost.com/feeds/posts/default?alt=rss",
    "http://www.iguessimfloating.net/category/video/feed",
    "http://smokedontsmoke.com/rss",
    "http://www.portalsmusic.com/category/sights/feed/",
    "http://feeds.feedburner.com/Sparkups?format=xml",
    "http://sonicmasala.blogspot.com/feeds/posts/default?alt=rss",
    "http://stadiumsandshrines.com/?feed=rss2&cat=1790",
    "http://www.thefader.com/category/music/videomusic/feed/",
    "http://yvynyl.tumblr.com/rss"
]

for url in blog_urls:
    crawler(url)
