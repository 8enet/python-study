__author__ = 'zl'
import urllib.parse
import http.client

from douban import config


def get_domain(url):
    if url is not None:
        return urllib.parse.splithost(urllib.parse.splittype(url)[1])[0]
    else:
        raise 'request url is None !!!'


def http_request(url):
    print('http_request  --> ', url)
    conn = http.client.HTTPConnection(get_domain(url))
    conn.request("GET", url, headers=config.HTTP_HEADERS)
    resp = conn.getresponse().read().decode("utf-8")
    return resp

def is_empty(text):
    return text is None or len(text) == 0

def match_people_url(url):
    if is_empty(url):
        return False
    return str(url).find('http://www.douban.com/group/people/') != -1
