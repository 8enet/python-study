__author__ = 'zl'

BASE_URL = "https://www.douban.com/group/{groupName}/discussion?start={startIndex}"
PEOPLE_ZONE_URL = 'http://www.douban.com/group/people/'
GROUPS = ['383972', '146409']  # 小组名称
MAX_PAGE = 7     # 最大页数
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
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36"
}
POSTS_KEY_WORD = ("大渡河路","金沙江路","长风公园","华师大","环球港")
#identity