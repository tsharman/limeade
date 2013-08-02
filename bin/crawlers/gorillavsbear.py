import BeautifulSoup
import requests
from utils import id_extractor, add_video

def gorillavsbear_crawler():
    r = requests.get('http://www.gorillavsbear.net/feed/')

    soup = BeautifulSoup.BeautifulSoup(r.text)

    for item in soup.findAll('item'):
        title = item.title.contents[0]
        if title[:5] == "video":
            title = title[7:]

        original_post = item.guid.string
        pub_date = item.pubdate.string
        for element in item.findAll(text=True):
            if isinstance(element, BeautifulSoup.CData):
                cdata_soup = BeautifulSoup.BeautifulSoup(element)
                
                iframe = cdata_soup.find("embed")
                if iframe != None:
                    video_id, video_source = id_extractor(iframe["src"])

                    if video_id == None:
                        continue
                    add_video(video_source, video_id, title, pub_date, original_post)

