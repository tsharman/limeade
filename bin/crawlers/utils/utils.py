from urlparse import urlparse
from pymongo import MongoClient
import time
from datetime import datetime
import requests
import BeautifulSoup
from db import *

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

def add_video(**kwargs):
    db = db_client()

    collected_data = {}

    if 'pub_date' in kwargs:
        pub_date_str = kwargs.get('pub_date')
        pub_date = datetime.strptime(pub_date_str[:-6], '%a, %d %b %Y %H:%M:%S')
        collected_data["latest_pubdate"] = pub_date

    # check to see if video already exists
    if 'video_id' in kwargs:
        video_id = kwargs.get('video_id')
        collected_data["video_id"] = video_id

        # checking to see if this video already exists
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
    
    if 'video_source' in kwargs:
        video_source = kwargs.get('video_source')
        if video_source == "vimeo":
            r = requests.get("http://vimeo.com/api/v2/video/" + video_id + ".xml")
            soup = BeautifulSoup.BeautifulSoup(r.text)
            video = soup.findAll('video')[0]
            
            title = video.title.string
            thumb = video.thumbnail_medium.string
        elif video_source == "youtube":
            r = requests.get("http://www.youtube.com/watch?v=" + video_id)
            soup = BeautifulSoup.BeautifulSoup(r.text)
            video = soup.find("span", { "id" :'eow-title'})
            title = video["title"]
        

    if "title" is not None:
        collected_data["title"] = title
        artist, track_name = title.split('-')
        if artist is not None and track_name is not None:
            print "ARTST"
            print artist
            print "TRACK_NAME"
            print track_name
            collected_data["artist"] = artist.rstrip(' ')
            collected_data["track_name"] = track_name.lstrip(' ')


    elif "title" in kwargs:
        collected_data["title"] = kwargs.get('title')
    
    if "video_source" in kwargs:
        collected_data["type"] = kwargs.get('video_source')

    if "original_post" in kwargs:
        collected_data["original_post"]  = kwargs.get('original_post')

    if thumb is not None:
        collected_data["thumb"] = thumb

    collected_data["blog_hits"] = 1

    try:
        new_video_id = db.videos.insert(collected_data)
        print collected_data
        print ("video added!" + video_id)
        return True
    except:
        pass
    return False

