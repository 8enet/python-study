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
    print('http_request  ', url)
    conn = http.client.HTTPConnection(get_domain(url))
    conn.request("GET", url, headers=config.HTTP_HEADERS)
    resp = conn.getresponse().read().decode("utf-8")
    return Resp(resp)

class Resp:
    def __init__(self, resp):
        self.resp = resp

    def __call__(self, *args, **kwargs):
        return self.resp
