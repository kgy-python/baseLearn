#!/usr/bin/env python 
# -*- coding:utf-8 -*-

__author__ = 'kgy'


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # 定义析构函数
    def __del__(self):
        print('del删除对象')


# 创建一个Item对象，将之赋给im变量
im = Item('鼠标', 29.8)
x = im  # ①
# 打印im所引用的Item对象
del im
print('--------------')
