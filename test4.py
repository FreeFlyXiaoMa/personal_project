#!/usr/bin/env python   # -*- coding: utf-8 -*-
# @Author  : Ma
# @Time    : 2020/12/31 11:03
# @File    : test4.py
def fast_sort(nums):
    if not nums :return
    print(nums)
    left = []
    right = []
    mid = len(nums) // 2
    # print('mid',mid)
    start = 0
    end = len(nums) - 1

    while start < end:
        if int(nums[start]) < int(nums[mid]):
            right.append(nums[start])
            print(right)
        else:
            start += 1
        if int(nums[end]) > int(nums[mid]):
            left.append(nums[end])

        else:
            end -= 1
        print(left)
        print(right)
        return fast_sort(left) + nums[mid] + fast_sort(right)


with open('./tlq/aa.txt','r',encoding='utf-8') as f:
    str_=f.read()
    list1=str_.split(' ')
    list2=[]
    for i in list1:
        if i.isdigit():
            list2.append(int(i))
    # list2.sort(reverse=True)
    list2=fast_sort(list2)
    print(list2[:10])









