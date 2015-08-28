__author__ = 'zl'

import concurrent.futures
import re

from demo.douban import config, utils, core

"""
房子不好找啊，定时抓取豆瓣上发布的合租或租房信息，过滤相关的条件，一旦有匹配的新贴子就发通知
目前完成度 多线程抓取贴子并解析数据,数据过滤,多个小组
然并卵啊，并没有合适的房源 (T＿T)
update 2015/08/28 11:04
"""

def main():
    urls = [config.BASE_URL.format(groupName=grp, startIndex=p*config.PAGE_SIZE)
            for grp in config.GROUPS
            for p in range(config.MAX_PAGE)
            ]

    with concurrent.futures.ThreadPoolExecutor(max_workers=config.MAX_THREAD) as executor:
        futures_http = {
            executor.submit(_work, url): url for url in urls
            }
        all_list = []
        for ft in concurrent.futures.as_completed(futures_http):
            url = futures_http[ft]
            try:
                curr_res = ft.result()
                all_list.extend(curr_res)
                call_result_success(url, curr_res)
            except Exception as e:
                call_result_fail(url, e)
                print(e)
        spider_completed(all_list)
    pass

def _work(url):
    resp = utils.http_request(url)
    return _parse_html(resp)

def _parse_html(resp):
    parser = core.MyHTMLParser()
    parser.feed(resp)
    return parser.getposts()

def call_result_success(url, posts):
    """
    单个任务执行完成
    :param url:
    :param posts: PostsInfo 列表
    :return:
    """
    pass


def call_result_fail(url, error):
    """
    单个任务失败
    :param url:
    :param error:
    :return:
    """
    print(url, error)
    pass

def spider_completed(datas):
    """
    所有任务全部完成
    :param datas: 所有PostsInfo列表
    :return:
    """
    if utils.is_empty(datas):
        pass
    rgx = _get_rgx()
    for post in datas:
        if rgx.search(post.to_string()) is not None:
            print(post.to_string())
    pass

def _get_rgx():
    reg = ''
    for k in config.POSTS_KEY_WORD:
        reg += '('+k+')|'
    return re.compile(r''+reg[:-1]+'', re.L)


if __name__ == "__main__":
    main()
