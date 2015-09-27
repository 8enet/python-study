__author__ = 'zl'


from proxy_provider import WWW_xicidaili_com


def main2():
    wx = WWW_xicidaili_com()
    res = wx.get_proxys(1, 2)
    print(res)
    pass

if __name__ == '__main__':
    main2()

