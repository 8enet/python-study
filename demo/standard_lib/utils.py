__author__ = 'zl'
import urllib.parse
import http.client
import threading

HTTP_HEADERS = {
    "Cache-Control": "max-age=0",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 \
                  (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36"
}

def get_domain(url):
    if url is not None:
        return urllib.parse.splithost(urllib.parse.splittype(url)[1])[0]
    else:
        raise ValueError('request url is None !!!')


def http_request(url):
    print('http_request  --> ', url, threading.current_thread().getName())
    conn = http.client.HTTPConnection(get_domain(url))
    conn.request("GET", url, headers=HTTP_HEADERS)
    resp = conn.getresponse().read().decode("utf-8")
    return resp

def is_empty(text):
    return text is None or len(text) == 0

