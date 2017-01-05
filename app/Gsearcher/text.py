import requests
from bs4 import BeautifulSoup
import re
import jieba
from app.Gsearcher.textrank import extractKeyphrases


class ExtractKeyWords:
    text_list = []
    word_set = set()

    def __init__(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
        }
        r = requests.get(url=url, headers=headers)
        html_content = r.text
        self.soup = BeautifulSoup(html_content, "html.parser")
        self.soup.prettify()

    def enplaintext(self):
        s = ''
        for t in self.soup.find_all('p'):
            s = t.get_text()
            # print(s)
            text_list = s.split(' ')
            if len(text_list) > 80:
                print(s)
                break
        try:
            return extractKeyphrases(s)
        except:
            return
            # if len(s) > 400:
            #     kw = extractKeyphrases(s)
            #     kw_list.append(kw)

    def zhplaintext(self):
        empty = re.compile(r'^\s*$')
        for t in self.soup.find_all(text=re.compile(r'^')):
            try:
                s1 = t.string
                if not empty.match(s1):
                    self.text_list.append(s1.strip())
            except:
                pass
        for t in self.soup.find_all('p'):
            try:
                s1 = t.string
                if len(s1) > 8:
                    it = jieba.cut(s1, cut_all=False)
                    for i in it:
                        self.word_set.add(i)
            except:
                pass
        return self.text_list

    def getplaintext(self, language):
        if language == 'en':
            return self.enplaintext()
        elif language == 'zh':
            return self.zhplaintext()

# uurl = 'https://en.wikipedia.org/wiki/Taj_Mahal'
# e = ExtractKeyWords(uurl)
# print(e.getplaintext('en'))
# count = 0
