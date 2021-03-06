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
    print('http_request  --> ', url)
    conn = http.client.HTTPSConnection(get_domain(url))
    conn.request("GET", url, headers=config.HTTP_HEADERS)
    http_response = conn.getresponse()
    resp_data = http_response.read()
    if http_response.getheader("Content-Encoding") == "gzip":
        return str(gzip.decompress(resp_data), "utf-8")
    else:
        return resp_data.decode("utf-8")


def is_empty(text):
    return text is None or len(text) == 0

def match_people_url(url):
    if is_empty(url):
        return False
    return str(url).find(config.PEOPLE_ZONE_URL) != -1
