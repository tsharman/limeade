from urlparse import urlparse
from pymongo import MongoClient
import time
from datetime import datetime
import requests
import BeautifulSoup

if os.environ.get('PROD') == None:
  from local_settings import *
else:
  mongo_db_uri = os.environ.get('MONGO_DB_URI')
  mongo_db_port = os.environ.get('MONGO_DB_PORT')

def youtube_id_extractor(youtube_url):
    query = urlparse(youtube_url)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            p = parse_qs(query.query)
            return p['v'][0]
        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            return query.path.split('/')[2]
    return None

def vimeo_id_extractor(vimeo_url):
    query = urlparse(vimeo_url)
    if query.hostname == 'player.vimeo.com':
        if query.path[:7] == '/video/':
            return query.path.split('/')[2]
    return None

def id_extractor(full_url):
    youtube_id = youtube_id_extractor(full_url)
    vimeo_id = vimeo_id_extractor(full_url)

    if youtube_id != None:
        return youtube_id, "youtube"
    if vimeo_id != None:
        return vimeo_id, "vimeo"
    return None, None


def db_client():
    client = MongoClient(mongo_db_uri, mongo_db_port)
    db = client['musicvideo']
    return db

def add_video(video_source, video_id, title, pub_date_str, original_post = None):
    db = db_client()
    
    pub_date = datetime.strptime(pub_date_str[:-6], '%a, %d %b %Y %H:%M:%S')
     
    # check to see if video already exists
    video_check = db.videos.find_one({'video_id' : video_id })
    if video_check:
        video_check_pubdate = video_check["latest_pubdate"]
        if (pub_date > video_check_pubdate):
            video_check["latest_pubdate"] = pub_date
            video_check["blog_hits"] = video_check["blog_hits"] + 1
            db.videos.save(video_check)
            print "video UPDATED"
            return True            
        else:
            print "video already exists!"
            return False

    thumb = None
    if video_source == "vimeo":
        r = requests.get("http://vimeo.com/api/v2/video/" + video_id + ".xml")
        soup = BeautifulSoup.BeautifulSoup(r.text)
        video = soup.findAll('video')[0]
        title = video.title.string
        thumb = video.thumbnail_medium.string

    video = {
        "type" : video_source,
        "video_id" : video_id,
        "title" : title,
        "original_post" : original_post,
        "latest_pubdate" : pub_date,
        "blog_hits" : 1,
        "thumbnail" : thumb,
    }
    
    
    try:
        new_video_id = db.videos.insert(video)
        print ("video added!" + video_id)
        return True
    except:
        pass
    return False

