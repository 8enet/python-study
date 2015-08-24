__author__ = 'zl'

import concurrent.futures
from html.parser import HTMLParser

from douban import config, utils
"""
房子不好找啊，定时抓取豆瓣上发布的合租或租房信息，过滤相关的条件，一旦有匹配的新贴子就发通知
目前完成度 多线程抓取贴子并解析数据
2015/08/24 23:26
"""

def main():
    urls = []
    for page in range(config.MAX_PAGE):
        urls.append(config.BASE_URL + str(page))

    with concurrent.futures.ThreadPoolExecutor(max_workers=config.MAX_THREAD) as executor:
        futures_http = {
            executor.submit(utils.http_request(url), url, 60): url for url in urls
            }
        for ft in concurrent.futures.as_completed(futures_http):
            url = futures_http[ft]
            try:
                call_result_success(url, ft.result())
            except Exception as e:
                call_resulr_fail(url, e)
                print(e)
    pass


def call_result_success(url, resp):
    # print(resp)
    parser = MyHTMLParser()
    parser.feed(resp)
    for post in parser.getposts():
        print(post.to_string())
    pass


def call_resulr_fail(url, error):
    print(url, error)
    pass


class PostsInfo():
    title = ''
    topic_url = ''
    author = ''
    last_time = ''

    def to_string(self):
        return 'title:'+self.title+'  author:'+self.author+'  time:'+self.last_time
    pass


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.posts = []
        self.curr_post = None
        self.is_new = False
        self.real_start = False
        self.is_title_ing = False
        self.is_author_ing = False
        self.is_time_ing = False

    def handle_starttag(self, tag, attrs):
        if self.real_start:
            if not self.is_new and tag == 'tr' and len(attrs) == 1 and attrs[0][0] == 'class' and attrs[0][1] == '':
                self.is_new = True
                self.curr_post = PostsInfo()
                pass

            if not self.is_title_ing and tag == 'td':
                if len(attrs) == 1 and attrs[0][0] == 'class' and attrs[0][1] == 'title':
                    self.is_title_ing = True
                    pass

            if self.is_title_ing and tag == 'a':
                self.curr_post.topic_url = attrs[0][1]
                self.curr_post.title = attrs[1][1]
                pass

            if tag == 'td' and len(attrs) == 2 and attrs[1][0] == 'class' and attrs[1][1] == 'time':
                self.is_time_ing = True

        else:
            can_nex = tag == 'table'
            if can_nex:
                for attr in attrs:
                    if len(attr) >= 2 and attr[0] == 'class' and attr[1] == 'olt':
                        self.real_start = True
                        break

    def handle_endtag(self, tag):
        if self.real_start and tag == 'table':
            self.real_start = False
            pass

        if self.is_new and tag == 'tr':
            self.is_new = False
            self.is_title_ing = False
            self.posts.append(self.curr_post)
            pass

        if self.is_title_ing and tag == 'td':
            self.is_title_ing = False
            pass
        if self.is_time_ing and tag == 'td':
            self.is_time_ing = False


    def handle_data(self, data):
        if self.is_time_ing:
            self.curr_post.last_time = data
        pass

    def getposts(self):
        return self.posts

if __name__ == "__main__":
    main()
