#!/usr/bin/env python 
# -*- coding:utf-8 -*-

__author__ = 'kgy'


class Person:
    """这是一个学习Python定义的一个Person类"""

    # 下面定义了一个类变量
    hair = 'black'

    def __init__(self, name='Charlie', age=8):
        # 下面为Person对象增加2个实例变量
        self.name = name
        self.age = age

    # 下面定义了一个say方法
    def say(self, content):
        print(content)


p = Person()
print(type(p))

# 输出p的name、age实例变量
print(p.name, p.age)  # Charlie 8
# 访问p的name实例变量，直接为该实例变量赋值
p.name = '李刚'
# 调用p的say()方法，声明say()方法时定义了2个形参
# 但第一个形参（self）是自动绑定的，因此调用该方法只需为第二个形参指定一个值
p.say('Python语言很简单，学习很容易！')
# 再次输出p的name、age实例变量
print(p.name, p.age)  # 李刚 8

