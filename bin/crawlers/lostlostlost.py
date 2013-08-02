import BeautifulSoup
import requests
from utils import id_extractor, add_video


def lostlostlost_crawler():
    r = requests.get('http://www.lostlostlost.com/feeds/posts/default?alt=rss')

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
            add_video(video_source, video_id, title, pub_date, original_post)

