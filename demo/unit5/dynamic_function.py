# 动态方法绑定
from types import MethodType


class User():
    __slots__ = ('set_name', 'name')  # 允许绑定到对象上的属性名称,绑定到类的没有此限制
    pass


def set_name(self, name):
    self.name = name


def set_id(self, id):
    self.id = id


def main():
    user = User()
    user.set_name = MethodType(set_name, user)  # 只绑定到对象
    user.set_name('abc')
    print(user.name)
    print(dir(user))

    User.set_id = MethodType(set_id, User)  # 绑定类
    user2 = User()
    user2.set_id(5)
    print(user2.id)

    print(dir(user2))

    pass


if __name__ == '__main__':
    main()
