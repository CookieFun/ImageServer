from app.Gsearcher.text import ExtractKeyWords
import re


class KeyWords:
    url_list = []
    keyword_list = []
    word_set = set()

    def __init__(self, url_list):
        zhpattern = re.compile(u'[\u4e00-\u9fa5]+')
        self.url_list = url_list
        for index, t in enumerate(url_list):
            url = t[1]
            print('-------')
            print(index, t[0][0])
            if zhpattern.search(t[0][0]):
                empty = {'no keywords'}
                self.keyword_list.append(empty)
                # self.word_list.append(y.getplaintext('zh'))
                # if first == 1:
                #     self.word_set = y.word_set
                #     first = 0
                # else:
                #     self.word_set = self.word_set & y.word_set
            else:
                y = ExtractKeyWords(url)
                res = y.getplaintext('en')
                self.keyword_list.append(res)
                print(res)
