#!/usr/bin/env python 
# -*- coding:utf-8 -*-

__author__ = 'kgy'

a_range = range(10)
a_list = [x * x for x in a_range]
print(a_list)

b_list = [x * x for x in a_range if x % 2 == 0]
print(b_list)
print(type(b_list))

c_generator = (x * x for x in a_range if x % 2 == 0)
print(type(c_generator))
for i in c_generator:
    print(i, end='\t')
print()

d_list = [(x, y) for x in range(5) for y in range(4)]
print(d_list)
