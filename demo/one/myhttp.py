__author__ = 'zl'
import http.client
import urllib.parse
import json
import threading
import os
import sys

HOST = "http://ip.taobao.com/service/getIpInfo2.php?ip=myip"


def request(url, func=None):
    """
    同步请求，会阻塞线程
    :param url: url路径
    :param func: 回调
    :return:
    """
    conn = http.client.HTTPConnection(get_domain(url))
    conn.request("GET", url)
    try:
        resp_str = conn.getresponse().read().decode()
        print(resp_str)
        if func is not None:
            func(json.loads(resp_str))
    except Exception as err:
        print(err)
    pass


def request_async(url, func=None):
    """
    异步请求
    :param url: 请求的url
    :param func: 回调
    :return:
    """
    threading.Thread(target=request, args=(url, func)).start()


def get_domain(url):
    """
    :param url: 完整的utl
    :return: 域名
    """
    if url is not None:
        return urllib.parse.splithost(urllib.parse.splittype(HOST)[1])[0]
    pass


def callback(resp_str):
    print(threading.current_thread().getName())
    print(resp_str)
    pass


def get_os_info():
    print(os.uname())
    print(sys.path)
