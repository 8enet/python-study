# 偏函数
import functools

def main():
    str='100000'
    i = int(str,base=8)
    print(i)
    print(int8(str))
    int8_=functools.partial(int,base=8)
    print(int8_(str))
    print(dir(int8_))
    pass

def int8(x,base=8):
    return int(x,base=base)

if __name__ == '__main__':
    main()