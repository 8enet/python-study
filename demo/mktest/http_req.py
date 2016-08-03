import requests
import urllib.parse
import json

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36',
    'DNT': '1',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8', 'Cache-Control': 'max-age=0',
    'Connection': 'close',
    'Referer': 'https://plus.google.com/',
    ':authority': 'translate.googleapis.com',
    ':method': 'GET',
    ':scheme': 'https',
}


def main():
    q = 'A wrapper library to simplify basic integrations with Google Play Services. The library wraps the following APIs (for now):'
    # r = requests.get('https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=zh-CN&hl=zh-CN&dt=t&dt=bd&dj=1&source=icon&tk=508745|535120&q=%s' % (urllib.parse.quote(q)))
    # s = r.text
    # print(s)
    # print(r.url)
    # st = s.index('"')+1
    # print(s[st:s.index('"', st)])
    google_translate(q)
    pass


def google_translate(q):
    q = urllib.parse.quote(q)
    path = '/translate_a/single?client=gtx&sl=auto&tl=zh-CN&hl=zh-CN&dt=t&dt=bd&dj=1&source=icon&tk=508745|535120&q=%s' % q
    HEADERS[':path'] = path
    r = requests.get('https://translate.googleapis.com' + path, HEADERS)
    data = json.loads(r.text)
    print(data)
    for item in data['sentences']:
        print(item['trans'])


if __name__ == '__main__':
    main()
