__author__ = 'zl'

BASE_URL = "http://www.douban.com/group/shanghaizufang/discussion?start="
MAX_PAGE = 3     # 最大页数
PAGE_SIZE = 25   # 每页条数
MAX_THREAD = 5   # 最多线程数
SAVE_PATH = ""
HTTP_HEADERS = {
    "Cache-Control": "max-age=0",
    "Host": "www.douban.com",
    "Referer": "http://www.douban.com/group",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36"
}
POSTS_KEY_WORD = ("闸北", "大宁", "上海马戏城", "1号线")
