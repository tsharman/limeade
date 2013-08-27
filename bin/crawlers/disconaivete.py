import BeautifulSoup
import requests
from utils.utils import id_extractor, add_video


def disco_naivete_crawler():
    r = requests.get('http://disconaivete.com/rss')

    soup = BeautifulSoup.BeautifulSoup(r.text)
    

    for item in soup.findAll('item'):
        title_raw = item.title.string
        prefix_check = title_raw[:5]
        if title_raw[:5] == "video":
            title = title_raw[7:]
        elif title_raw[:6] == "stream":
            title = title_raw[8:]
        else:
            title = title_raw
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

