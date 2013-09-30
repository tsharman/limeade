import BeautifulSoup
import requests
from utils.utils import id_extractor, add_video



def crawler(url):
    r = requests.get(url)
    soup = BeautifulSoup.BeautifulSoup(r.text)
    
    for item in soup.findAll('item'):
        original_post = item.guid.string
        if original_post is None:
            print "Error! Missing original_post"
            continue

        pub_date = item.pubdate.string
        
        if original_post is None:
            print "Error! Missing pub_date"
            continue

        # extracting id
        
        video_source = None
        video_id = None
        if video_source is None or video_id is None:
            try:
                desc_soup = BeautifulSoup.BeautifulSoup(item.description.string, convertEntities=BeautifulSoup.BeautifulSoup.HTML_ENTITIES)
                desc_soup = BeautifulSoup.BeautifulSoup(desc_soup.contents[0])
                iframe = desc_soup.find("iframe")
                if iframe != None:
                    video_id, video_source = id_extractor(iframe["src"])
            except:
                pass

        if video_source is None or video_id is None:
            try:
                for element in item.findAll(text=True):
                    if isinstance(element, BeautifulSoup.CData):
                        cdata_soup = BeautifulSoup.BeautifulSoup(element)
                        iframe = cdata_soup.find("iframe")
                        if iframe != None:
                            video_id, video_source = id_extractor(iframe["src"])
            except:
                pass

        if video_source is not None and video_id is not None:
            print original_post
            add_video(
                    video_source = video_source, 
                    video_id = video_id, 
                    pub_date = pub_date, 
                    original_post = original_post)
