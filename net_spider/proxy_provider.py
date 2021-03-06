from bs4 import BeautifulSoup
import requests
import concurrent.futures.thread
from datetime import datetime
from functools import wraps
import time
import json

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36',
    'Host': 'www.xicidaili.com', 'DNT': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch', 'Accept-Language': 'zh-CN,zh;q=0.8', 'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive'}


class ProxyInfo:
    def __init__(self, ip, port, type, desc):
        self.ip = ip
        self.port = port
        self.type = type
        self.desc = desc
        self.time = None

    def get_url(self):
        return '%s://%s:%s' % (str.lower(self.type), self.ip, self.port)

    def is_http(self):
        return str.lower(self.type) == 'http'

    def is_https(self):
        return str.lower(self.type) == 'https'

    def __repr__(self):
        return 'ip:%s:%s  type:%s  %s, time %s' % (self.ip, self.port, self.type, self.desc, self.time)


def use_req_time(func):
    @wraps(func)
    def wrap_req(proxyinfo):
        t0 = time.time()
        result = func(proxyinfo)
        t1 = time.time()
        proxyinfo.time = t1-t0
        return result
    return wrap_req


@use_req_time
def check_proxy(proxyinfo):
    try:
        r = requests.get('http://ip.taobao.com/service/getIpInfo2.php?ip=myip', headers=HEADERS, timeout=30,
                         proxies={str.lower(proxyinfo.type): proxyinfo.get_url()})
        if r.status_code == 200:
            try:
                r.encoding = 'utf-8'
                json.loads(r.text)
                return proxyinfo
            except Exception:
                pass
    except Exception:
        pass

def _request_page(url, proxies=None):
    r = requests.get(url, headers=HEADERS, proxies=proxies)
    r.encoding = 'utf-8'
    return r.text

class ProxyPage:
    def __init__(self):
        self.main_url = None
        self.urls = None
        self.proxys = None

    def _to_impl(self):
        raise RuntimeError('please impl this class')

    def get_proxys(self,start, end, proxies=None):
        self._to_impl()

class WWW_xicidaili_com(ProxyPage):

    def __init__(self):
        super().__init__()
        self.main_url = 'http://www.xicidaili.com/nt/{page}'

    def get_proxys(self, start, end, proxies=None):
        self.urls = [self.main_url.format(page=i) for i in range(start, end)]

        def parse(tag):
            tds = tag.find_all('td')
            return ProxyInfo(tds[2].text, tds[3].text, tds[6].text, tds[4].text)
        with concurrent.futures.thread.ThreadPoolExecutor(max_workers=50) as executor:
            futures = [executor.submit(_request_page, url, proxies) for url in self.urls]
            res = []
            for ft in concurrent.futures.as_completed(futures):
                try:
                    curr_res = ft.result()
                    soup = BeautifulSoup(curr_res, "lxml")
                    tag = soup.find(id='ip_list').find_all('tr')
                    res.extend([parse(next) for next in tag
                                if next.find('img') is not None])
                except Exception as e:
                    pass
            print('start check proxy ...')
            futures = [executor.submit(check_proxy, info) for info in filter(lambda pinfo: pinfo.is_http(), res)]
            print('check proxy size %s ' % (len(futures)))
            st = datetime.now()
            res = [ft.result() for ft in concurrent.futures.as_completed(futures) if ft.result() is not None]
            print('check proxy over ,success proxy size %s , free time %s ' % (len(res), datetime.now()-st))
            return res

        pass