#!/usr/bin/env python 
# -*- coding:utf-8 -*-

__author__ = 'kgy'

s_max = input("请输入您想计算的阶乘:")
mx = int(s_max)
result = 1
# 使用for-in循环遍历范围
for num in range(1, mx + 1):
    result *= num
print(result)

src_list = [12, 45, 3.4, 13, 'a', 4, 56, 'crazyit', 109.5]
my_sum = 0
my_count = 0
for ele in src_list:
    # 如果该元素是整数或浮点数
    if isinstance(ele, int) or isinstance(ele, float):
        print(ele)
        my_sum += ele
        my_count += 1

print('总和:', my_sum)
print('平均数:', my_sum / my_count)

my_dict = {'语文': 89, '数学': 92, '英语': 80}
# 通过items()方法遍历所有key-value对
# 由于items方法返回的列表元素是key-value对，因此要声明两个变量
print(my_dict.items())
for key, value in my_dict.items():
    print('key:', key)
    print('value:', value)
print('-------------')
# 通过keys()方法遍历所有key
for key in my_dict.keys():
    print('key:', key)
    # 在通过key获取value
    print('value:', my_dict[key])
print('-------------')
# 通过values()方法遍历所有value
for value in my_dict.values():
    print('value:', value)

src_list = [12, 45, 3.4, 12, 'fkit', 45, 3.4, 'fkit', 45, 3.4]
statistics = {}
for ele in src_list:
    # 如果字典中包含ele代表的key
    if ele in statistics:
        # 将ele元素代表出现次数加1
        statistics[ele] += 1
    # 如果字典中不包含ele代表的key，说明该元素还未出现国
    else:
        # 将ele元素代表出现次数设为1
        statistics[ele] = 1
    # 遍历dict，打印出各元素的出现次数
for ele, count in statistics.items():
    print("%s的出现次数为:%d" % (ele, count))
