import sys
import requests
from bs4 import BeautifulSoup
import importlib
from app.Gsearcher.crosspage_keyword import KeyWords

importlib.reload(sys)


class Searcher:
    # each element in getSearchList is a three-elements tuple, (title, url, keywords)
    # title is a list contains at least one string
    # url is a single string
    # keywords is a dictionary of several strings, Chinese result is {'no keywords'}
    g_url = 'https://www.google.com'
    g_imageUrl = 'https://www.google.com/searchbyimage?site=search&sa=X&image_url='
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
    }

    def __init__(self, image_url):
        image_searchUrl = Searcher.g_imageUrl + image_url
        response = requests.get(url=image_searchUrl, headers=Searcher.headers)
        self.soup = BeautifulSoup(response.text, "html.parser")
        # self.soup = BeautifulSoup(open('Google Search.htm'), "html.parser")

    def getGuest(self):
        best_guest = self.soup.find('a', class_="_gUb")
        best_guest_content = best_guest.contents
        best_guest_href = Searcher.g_url + best_guest.get('href')
        return (best_guest_content, best_guest_href)

    def getSearchList(self):
        result_list = []
        search_results = self.soup.find_all('h3', class_="r")[:3]
        for r in search_results:
            tag_href = r.find('a')
            content = tag_href.contents
            href = tag_href.get('href')
            result_list.append((content, href))
        result_list=result_list[0:3]
        kw = KeyWords(result_list)
        temp = []
        for index, t in enumerate(result_list):
            temp.append((t[0], t[1], kw.keyword_list[index]))
        return temp


# image_url = 'http://cdn.sstatic.net/Sites/stackoverflow/company/img/logos/so/so-icon.png'
# image_url = 'http://www.history.com/s3static/video-thumbnails/AETN-History_VMS/21/115/History_Engineering_the_Taj_Mahal_42712_reSF_HD_still_624x352.jpg'
# IS = Searcher(image_url)
# f = open('result.html', 'w', encoding='utf-8')
# f.write(IS.soup.prettify())
# print(IS.getGuest())
# print(IS.getSearchList())
# f.close()

