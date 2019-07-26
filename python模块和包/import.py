#!/usr/bin/env python 
# -*- coding:utf-8 -*-

__author__ = 'kgy'

# 导入sys整个模块，并指定别名为s
import sys as s

# 使用s模块别名作为前缀来访问模块中的成员
print(s.argv[0])

# 导入sys模块的argv成员，并为其指定别名v
from sys import argv as v

# 使用导入成员（并指定别名）的语法，直接使用成员的别名访问
print(v[0])
