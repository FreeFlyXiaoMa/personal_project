#!/usr/bin/env python   # -*- coding: utf-8 -*-
# @Author  : Ma
# @Time    : 2021/1/2 17:45
# @File    : test1.py
# Input='aabcdbefgde'
#
# child_list=[]
# for i in range(len(Input)-1):
#     for j in range(i+1,len(Input)):
#         child_list.append(Input[i:j+1])
#
# list1=[]
# for k in child_list:
#     if len(k) == len(set(k)):
#         list1.append(k)
# del  child_list
#
# hash_={}
# max_len=0
# for m in list1:
#     hash_[m]=len(m)
#     if len(m) > max_len:
#         max_len=len(m)
#
# for key,val in hash_.items():
#     if val  ==  max_len:
#         print(key)


class queue(object):
    def __init__(self):
        super(queue, self).__init__()
        self.queue=[]

    def push(self,x):
        self.queue.append(x)

    def pop(self):
        if self.queue:
            return self.queue.pop(0)

    def length(self):
        return len(self.queue)

queue=queue()
queue.push(2)
queue.push(3)
queue.push(19)
pop_val=queue.pop()
print('pop_val:',pop_val)
print('length:',queue.length())
