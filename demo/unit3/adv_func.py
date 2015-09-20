__author__ = 'zl'

from functools import reduce
import math

"""
python 高阶函数 Higher-order function
"""

def f_map1():
    """
    map() 函数  每一项单独取出来处理作用在函数上
    :return:
    """
    # 将一个list 每项 x2
    ls = [2, 4, 5, 1, 8]

    def x2(i):
        return i*2
    # r = map(x2, ls)
    r = map(lambda x:x*2, ls)
    print(list(r))

def f_reduce1():
    """
    map() 函数，把结果和下一项作用在函数上
    :return:
    """
    ls = [2, 4, 5, 1, 8]
    # 求这个list之和

    def c(x,n):
        return x+n
    r = reduce(c,ls)
    r = reduce(lambda x,n:x+n, ls)
    print(r)

def f_sorted1():
    """
    sorted() 函数，排序
    :return:
    """
    ls = [2, 4, -5, 1, 8]
    r = sorted(ls, key=abs) # 根据绝对值排序
    print(r)
    ls = ['az', 'Vg', '6d', 'ZR']
    r = sorted(ls, key=lambda x: str.lower(x))  # 忽略大小写排序
    print(r)
    data = [('ab', 34), ('Vg', 57), ('ZR', 76), ('az', 33)]
    r = sorted(data, key=lambda x: str.lower(x[0]))  # 根据第0项排序
    print(r)

def f_filter1():
    """
    filter() 函数，过滤
    :return:
    """
    # 回数 两边读都是一样的
    ls = filter(is_palindrome, range(1, 1000))
    print(list(ls))
    pass

def is_palindrome(num):
    s = int(math.log10(num)+1)  # 数字长度
    if s == 1:
        return False

    # 取数字的某一位，从右开始
    def get_v(i):
        return int((num % (10 ** i)) / 10 ** (i-1))
    x, y = s, 1
    while True:
        if get_v(x) == get_v(y):
            x -= 1
            y += 1
        else:
            return False

        if x <= y:
            return True


def main():
    f_map1()
    f_reduce1()
    f_sorted1()
    f_filter1()


if __name__ == '__main__':
    main()