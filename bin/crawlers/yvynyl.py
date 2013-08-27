import BeautifulSoup
import requests
from utils.utils import id_extractor, add_video


def yvynyl_crawler():
    r = requests.get('http://yvynyl.tumblr.com/rss')

    soup = BeautifulSoup.BeautifulSoup(r.text)

    for item in soup.findAll('item'):
        title = item.title.string
        original_post = item.guid.string
        pub_date = item.pubdate.string
        desc_soup = BeautifulSoup.BeautifulSoup(item.description.string, convertEntities=BeautifulSoup.BeautifulSoup.HTML_ENTITIES)
        desc_soup = BeautifulSoup.BeautifulSoup(desc_soup.contents[0])
        iframe = desc_soup.find("iframe")
        if iframe != None:
            video_id, video_source = id_extractor(iframe["src"])
            
            if video_id == None:
                continue
            add_video(
                video_source = video_source, 
                video_id = video_id, 
                title = title, 
                pub_date = pub_date, 
                original_post = original_post)

