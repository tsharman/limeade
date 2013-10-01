#!/var/www/musicvideo/env/bin/python

from crawler import crawler

blog_urls = [
    ( "http://www.blogotheque.net/feed/", "blogotheque" ),
    ( "http://www.gorillavsbear.net/feed/", "gorilla vs bear" ),
    ( "http://disconaivete.com/rss", "disconaivete" ),
    ( "http://www.iguessimfloating.net/category/video/feed", "i guess i'm floating" ),
    ( "http://smokedontsmoke.com/rss", "smoke don't smoke" ),
    ( "http://www.portalsmusic.com/category/sights/feed/", "portals" ),
    ( "http://feeds.feedburner.com/Sparkups?format=xml", "sparkups" ),
    ( "http://sonicmasala.blogspot.com/feeds/posts/default?alt=rss", "sonic masala" ),
    ( "http://stadiumsandshrines.com/?feed=rss2&cat=1790", "stadiums and shrines" ),
    ( "http://www.thefader.com/category/music/videomusic/feed/", "the fader" ),
    ( "http://yvynyl.tumblr.com/rss", "yvynyl" ),
    ( "http://yourstru.ly/blog/feed/", "yours truly"),
]

for url in blog_urls:
    crawler(url[0])
