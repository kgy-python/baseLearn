#!/usr/bin/env python 
# -*- coding:utf-8 -*-

__author__ = 'kgy'


class User:
    def __hide(self):
        print('示范隐藏的hide方法')

    def getname(self):
        return self.__name

    def setname(self, name):
        if len(name) < 3 or len(name) > 8:
            raise ValueError('用户名长度必须在3～8之间')
        self.__name = name

    name = property(getname, setname)

    def setage(self, age):
        if age < 18 or age > 70:
            raise ValueError('用户名年龄必须在18在70之间')
        self.__age = age

    def getage(self):
        return self.__age

    age = property(getage, setage)


# 创建User对象
u = User()
# 对name属性赋值，实际上调用setname()方法
# u.name = 'fk'  # 引发 ValueError: 用户名长度必须在3～8之间
u.name = 'fkit'
u.age = 25
print(u.name)
print(u.age)


class BaseClass:
    def foo(self):
        print('父类中定义的foo方法')


class SubClass(BaseClass):
    # 重写父类的foo方法
    def foo(self):
        print('子类重写父类中的foo方法')

    def bar(self):
        print('执行bar方法')
        # 直接执行foo方法，将会调用子类重写之后的foo()方法
        self.foo()
        # 使用类名调用实例方法（未绑定方法）调用父类被重写的方法
        BaseClass.foo(self)


sc = SubClass()
sc.bar()


class Role:
    pass


r = Role()
# 查看变量r的类型
print(type(r))  # <class '__main__.Role'>
# 查看Role类本身的类型
print(type(Role))  # <class 'type'>
