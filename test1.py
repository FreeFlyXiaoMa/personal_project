#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/18 21:07
# @Author  : Ma
# @File    : test1.py
# @Software: PyCharm

arr=[]


def quick_sort(arr):
    if len(arr) < 2: return arr

    mid = arr[len(arr) // 2]  # 基准值
    left, right = [], []  # 定义左右两个子列

    arr.pop(len(arr) // 2)  # 去掉这个基准值

    for item in arr:
        if item > mid:
            right.append(item)  # 大的放在右边
        else:
            left.append(item)  # 小的放在左边

    return quick_sort(left) + [mid] + quick_sort(right)  # 不断进行迭代

b = [11, 99, 33, 69, 77, 88, 55, 11, 33, 36, 39, 66, 44, 22]
re=quick_sort(b)
print('b:',b)
print('排序后:',re)


re.reverse()
print(re)