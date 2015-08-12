__author__ = 'zl'
import random
import sys

sys.setrecursionlimit(10000)  # 设置递归深度,如果不设置很大深度的情况下可能报错
# 类型和参数
# 元组用(),list用[],读取方法相同，区别是元组不可以改变而list可以，都支持切片[:]

def params_check(par1, par2, par3, *par4, **par5):
    """
    参数检查
    :param par1:
    :param par2:
    :param par3:
    :param par4: 可变参数，任意类型的元组,一般在最后
    :param par5: 自定义key-value的参数，如果和4同时出现，必须在4之后
    :return:
    """
    if isinstance(par1, int):  # 检测类型
        print("par1 is ok")
    else:
        raise TypeError("par1 type error")  # 抛出异常

    if isinstance(par2, (int, float)):  # 可以有多个类型，任何一种即可
        print("par2 is ok")

    print(par1, par2, par3, par4, par5)
    type_check()
    type_check()
    print(type_check())

    # 都能用切片
    v1 = (1, 2, 3)
    print(v1[:1])
    v2 = [4, 5, 6]
    print(v2[:1])
    pass


def type_check(par1=[]):  # 可以有默认参数，但是注意默认参数也是一个对象，
    # 比如这里的[]多次调用会叠加的,建议不要用这种可变对象当做默认参数的纸
    par1.append(random.Random().randint(0, 10))
    return par1


def recursive(x):
    if x == 1:
        return 1
    return x * recursive(x - 1)


def more_return_value(a, b):
    """
    多返回值，其实返回的是包装好的元组
    :param a:
    :param b:
    :return: 如果用多个变量的方式接收，必须出现相同多个接收变量，也可以当做元组下标访问
    """
    return a + b, a - b, a * b, a / b


def main():
    params_check(4, 2.9, 3, [4, 5, 6], {7: 8, 9: 10}, a=1, b=2)
    w, x, y, z = more_return_value(4, 5)
    print(w, x, y, z)
    print(more_return_value(6, 7)[0])
    pass


if __name__ == "__main__":
    main()
