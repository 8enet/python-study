__author__ = 'zl'
import sys

import myhttp

HOST = "http://ip.taobao.com/service/getIpInfo2.php?ip=myip"

def my_cus_http():
    myhttp.request(HOST, callback)

def callback(resp):
    print("---sadasd---")
    print(resp)

def my_os_env():
    print(sys.path)
    str = input("input:")
    print("---", str)


if __name__ == '__main__':
    #my_cus_http()
    my_os_env()