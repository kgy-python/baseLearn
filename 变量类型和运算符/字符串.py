#!/usr/bin/env python 
# -*- coding:utf-8 -*-

__author__ = 'kgy'

s2 = "Python "
s3 = "iS Funny"
# 使用+拼接字符串
s4 = s2 + s3
print(s4)

s1 = "这是数字: "
p = 99.8
# 字符串直接拼接数值，程序报错
# print(s1 + p)
# 使用str()将数值转换成字符串
print(s1 + str(p))
# 使用repr()将数值转换成字符串
print(s1 + repr(p))

# msg = input("请输入你的值：")
# print(type(msg))
# print(msg)

# Python长字符串
s = '''"Let's go fishing", said Mary.
"OK, Let's go", said her brother.
they walked to a lake'''
print(s)

# Python原始字符串
s1 = r'G:\publish\codes\02\2.4'
print(s1)

s = 'crazyit.org is very good'
# 获取s中索引2处的字符
print(s[2])  # 输出a
# 获取s中从右边开始，索引4处的字符
print(s[-4])  # 输出g
