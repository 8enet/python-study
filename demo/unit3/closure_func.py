__author__ = 'zl'
"""
closure 闭包
"""


def main():
    t1(1,2,3)
    pass

def check(fn):
    def new(*kwargs):
        print('wrap')
        return fn(kwargs)
    return new

@check
def t1(*kwargs):
    print(kwargs)

if __name__ == '__main__':
    main()