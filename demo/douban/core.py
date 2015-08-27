__author__ = 'zl'
from html.parser import HTMLParser
from demo.douban import utils

class PostsInfo():
    title = ''
    topic_url = ''
    author = ''
    last_time = ''

    def to_string(self):
        return 'title:'+self.title+'\tauthor:'+self.author+'\ttime:'+self.last_time+'\turl:'+self.topic_url
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
                pass

            if tag == 'a' and len(attrs) == 2 and attrs[0][0] == 'href' and utils.match_people_url(attrs[0][1]):
                self.is_author_ing = True

        else:
            can_nex = tag == 'table'
            if can_nex:
                for attr in attrs:
                    if len(attr) >= 2 and attr[0] == 'class' and attr[1] == 'olt':
                        self.real_start = True
                        break
        pass

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
            pass
        if self.is_author_ing and tag == 'a':
            self.is_author_ing = False

    def handle_data(self, data):
        if self.is_time_ing:
            self.curr_post.last_time = data
            pass
        if self.is_author_ing:
            self.curr_post.author = data
        pass

    def getposts(self):
        return self.posts
