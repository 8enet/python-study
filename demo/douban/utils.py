__author__ = 'zl'
import urllib.parse
import http.client
import threading
import gzip

from demo.douban import config


def get_domain(url):
    if url is not None:
        return urllib.parse.splithost(urllib.parse.splittype(url)[1])[0]
    else:
        raise ValueError('request url is None !!!')


def http_request(url):
    print('http_request  --> ', url, threading.current_thread().getName())
    conn = http.client.HTTPSConnection(get_domain(url))
    conn.request("GET", url, headers=config.HTTP_HEADERS)
    http_response = conn.getresponse()
    if http_response.getheader("Content-Encoding") == "gzip":
        resp = str(gzip.decompress(http_response.read()), "utf-8")
        return resp

    return http_response.read().decode("utf-8")


def is_empty(text):
    return text is None or len(text) == 0

def match_people_url(url):
    if is_empty(url):
        return False
    return str(url).find(config.PEOPLE_ZONE_URL) != -1
