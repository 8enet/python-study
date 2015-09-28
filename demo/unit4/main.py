__author__ = 'zl'

import sqlite3
import re
import urllib.parse
from bs4 import BeautifulSoup
import requests
import concurrent.futures.thread
import itertools


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36',
    'DNT': '1',
    'Host': 'www.baidu.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive'
}

_ALL_BLOCK = ['.*']

block_domain = {'baidu.com': ['.*.baidu.com', 'dev.baidu.com'],
                'google.com': ['.*.google.com', 'play.google.com'],
                'csdn.net': _ALL_BLOCK,
                'qq.com': _ALL_BLOCK  # 完全忽略
                }

_block_domain_re = {k: list((re.compile(r''+s+'', re.I) for s in v))
                    for k, v in block_domain.items()}

topHostPostfix = (
    '.com', '.la', '.io', '.co', '.info', '.net', '.org', '.me', '.mobi',
    '.us', '.biz', '.xxx', '.ca', '.co.jp', '.com.cn', '.net.cn',
    '.org.cn', '.mx', '.tv', '.ws', '.ag', '.com.ag', '.net.ag',
    '.org.ag', '.am', '.asia', '.at', '.be', '.com.br', '.net.br',
    '.bz', '.com.bz', '.net.bz', '.cc', '.com.co', '.net.co',
    '.nom.co', '.de', '.es', '.com.es', '.nom.es', '.org.es',
    '.eu', '.fm', '.fr', '.gs', '.in', '.co.in', '.firm.in', '.gen.in',
    '.ind.in', '.net.in', '.org.in', '.it', '.jobs', '.jp', '.ms',
    '.com.mx', '.nl', '.nu', '.co.nz', '.net.nz', '.org.nz',
    '.se', '.tc', '.tk', '.tw', '.com.tw', '.idv.tw', '.org.tw',
    '.hk', '.co.uk', '.me.uk', '.org.uk', '.vg', ".com.hk")
regx = r'[^\.]+(' + '|'.join([h.replace('.', r'\.') for h in topHostPostfix]) + ')$'
pattern = re.compile(regx, re.I)

def get_domain(domain):
    m = pattern.search(domain)
    res = m.group() if m else domain
    return res if res else None

def search(wd, pn=0):
    r = requests.get(str('https://www.baidu.com/s?wd={wd}&pn={pn}').format(wd=wd, pn=pn),
                     headers=HEADERS)
    r.encoding = 'utf-8'
    tag = BeautifulSoup(r.text, "lxml").select('div.result.c-container')
    res = [SearchResult.parse(item) for item in tag]
    return [s for s in res if s and not match_domain(s.short_url)]

def match_domain(domain):
    rd = get_domain(domain)
    if rd:
        if rd in _block_domain_re:
            for mx in _block_domain_re[rd]:
                return mx.match(domain)
    return False



class SearchResult:
    def __init__(self):
        self.title = None
        self.url = None
        self.short_url = None

    def __repr__(self):
        return 'title:%s  short_url:%s url:%s' % (self.title, self.short_url, self.url)

    @staticmethod
    def parse(text):
        result = SearchResult()
        try:
            a_tag = text.select('h3.t a')[0]
            result.title = a_tag.text
            result.url = a_tag.attrs['href']
        except Exception as e:
            print(e)
            return None
        try:
            result.short_url = text.select('div.f13 span.g')[0].text.split('/')[0]
        except Exception as e:
            print(e)
            return None
        return result

def main():
    wd = 'chrome site:zol.com.cn'
    max_pn = 100

    with concurrent.futures.thread.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(search, urllib.parse.quote(wd), pn)
                   for pn in range(0, max_pn, 10)]
        res = (item for l in (ft.result()
                              for ft in concurrent.futures.as_completed(futures)
                              if ft)
               for item in l)
        # or use itertools
        # res = list(itertools.chain.from_iterable(ft.result()
        #                                          for ft in concurrent.futures.as_completed(futures)
        #                                          if ft))

    if res is not None:
        with sqlite3.connect('search_result.db') as conn:
            cursor = conn.cursor()
            cursor.execute('drop table if exists tb_result ')
            cursor.execute('create table if not exists  tb_result '
                           '(short_url text primary key , title text not null, url text)')
            for info in res:
                try:
                    print(info)
                    cursor.execute("insert into tb_result(`short_url`,`url`,`title`) values (?,?,?)", (info.short_url, info.title, info.url))
                except sqlite3.IntegrityError as e:
                    pass
                except Exception as e:
                    print(e)

            conn.commit()



if __name__ == '__main__':
    main()
