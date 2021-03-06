from bs4 import BeautifulSoup
from demo.standard_lib import utils
"""
Beautiful Soup 4 示例
"""
url = "http://www.cnbeta.com"
def main():
    resp = utils.http_request(url)
    soup = BeautifulSoup(resp, "lxml")
    get_all_cus_text(soup)

def get_all_cus_text(soup):
    """
    获取所有类似子节点A 标签的数据 <div class='title'> <a href='a'>text</a> </div>
    :param soup:
    :return:
    """
    # soup.find() 只会返回第一个匹配的节点
    tag = soup.find_all('div', {'class', 'title'})
    for child in tag:
        print(child.a.text, url+child.a['href'])


if __name__ == '__main__':
    main()
