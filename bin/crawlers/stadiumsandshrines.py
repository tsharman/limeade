import BeautifulSoup
import requests
from utils.utils import id_extractor, add_video


def stadiumsandshrines_crawler():
    r = requests.get('http://stadiumsandshrines.com/?feed=rss2&cat=1790')

    soup = BeautifulSoup.BeautifulSoup(r.text)

    for item in soup.findAll('item'):
        title = item.title.string
        original_post = item.guid.string        
        pub_date = item.pubdate.string
        for element in item.findAll(text=True):
            if isinstance(element, BeautifulSoup.CData):
                cdata_soup = BeautifulSoup.BeautifulSoup(element)
                iframe = cdata_soup.find("iframe")
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

