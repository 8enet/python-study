__author__ = 'zl'

BASE_URL = "https://www.douban.com/group/{groupName}/discussion?start={startIndex}"
PEOPLE_ZONE_URL = 'http://www.douban.com/group/people/'
GROUPS = ['383972', '146409']  # 小组名称
MAX_PAGE = 5     # 最大页数
PAGE_SIZE = 25   # 每页条数
MAX_THREAD = 10   # 最多线程数
SAVE_PATH = ""
HTTP_HEADERS = {
    "Host": "www.douban.com",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "DNT": "1",
    "Upgrade-Insecure-Requests": "1",
    "Connection": "keep-alive",
    "Cookie": """ll="108296"; bid="xdZ+gOxaWtI"; _ga=GA1.2.2042841106.1411525252; ps=y; ct=y; _vwo_uuid_v2=D3DBEDA44FF0461728D3A6208DA98AB2|817c7abe3ca911e190d74a5f124201c8; ue="zlcn2200@yeah.net"; dbcl2="69727989:Fa4FGyv4V28"; ck=_1LW; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1470189488%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dcj8D-e0bmhdORwx6QunTx14ZGU5vHMtu1xT996y_Mxy%26wd%3D%26eqid%3D8af563c90000a8150000000457989b6d%22%5D; __utmt=1; ap=1; push_noty_num=0; push_doumail_num=0; _pk_id.100001.8cb4=71d8f6e877340b88.1425872199.85.1470194325.1470135906.; _pk_ses.100001.8cb4=*; __utma=30149280.2042841106.1411525252.1470135774.1470189493.105; __utmb=30149280.194.6.1470194325659; __utmc=30149280; __utmz=30149280.1470034752.99.70.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmv=30149280.6972""",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36"
}
POSTS_KEY_WORD = ("大渡河路","金沙江路")
#identity