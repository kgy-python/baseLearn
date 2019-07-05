#!/usr/bin/env python 
# -*- coding:utf-8 -*-

__author__ = 'kgy'

# 定义一个数值类型变量
a = 5
print(a)
print(type(a))
# 重新将字符串赋值给a变量
a = 'Hello , Charlie'
print(a)
print(type(a))

f = open("poem.txt", "w", encoding="utf-8")  # 打开文件以便写入
print('沧海月明珠有泪', file=f)
print('蓝回日暖玉生烟', file=f)
f.close()
