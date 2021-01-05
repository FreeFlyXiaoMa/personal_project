# #!/usr/bin/env python   # -*- coding: utf-8 -*-
# # @Author  : Ma
# # @Time    : 2020/12/26 11:24
# # @File    : one.py
#
# # strings='XSUWHQ'
# #
# # # print(len(strings.split(' ')[-1]))
# #
# # while True:
# #     try:
# #         s=input()
# #         while len(s) >8:
# #             print(s[:8])
# #             s=s[8:]
# #         if len(s) < 8:
# #             append_s='0'*(8-len(s))
# #             s+=append_s
# #             print(s)
# #     except:
# #         break
#
# # def find_prime(nums):
# #     prime_flag=1
# #     for i in range(2,int(nums**0.5 + 2)):
# #         if nums % i == 0:
# #             prime_flag=0
# #             print(i,end=' ')
# #             find_prime(nums/i)
# #             break
# #     if prime_flag:
# #         print(nums,end=' ')
# # find_prime(93938)
#
#
# # print(int(0.8))
#
# N = int(input())
# hash_v = {}
# for i in range(N):
#     ss = input()
#     key, val = int(ss.split(' ')[0]), int(ss.split(' ')[1])
#
#     hash_v[key] = hash_v.get(key,0) + val
# result = sorted(hash_v.keys(), reverse=False)
# for j in result:
#     print(j,hash_v[j])


# hash_={}
# result=[]
# num=input()
# for i in range(len(num) -1 ,-1,-1):
#     tmp=hash_.get(num[i],0)+1
#     hash_[num[i]]=tmp
#     if tmp ==1:
#         result.append(num[i])
# for j in result:
#     print(j,end='')
# print(result)

# sorted()

# s=input()
# new_str=''
# for i in s:
#     if i.islower() or i.isdigit():
#         new_str += i
#     elif i.isupper():
#         i=i.lower()-str(1)
#         new_str += i
# print(new_str)
# print(ord('a'))
# print(chr(97))



# from functools import wraps
# def My_decorate(f):
#     @wraps(f)
#     def fn(*args,**kwargs):
#         print('decorate called')
#         return f(*args,**kwargs)
#     return fn
# @My_decorate
# def fx():
#     print('fx called')
# fx()

import threading
import time
# n=[0]
# def foo():
#     n[0]=n[0] +1
#     n[0]=n[0]+1
#
# threads=[]
#
# for i in range(50000):
#     t=threading.Thread(target=foo)
#     threads.append(t)
# for t in threads:
#     t.start()
# print(n)

from threading import Thread

def my_counter():
    i=0
    for _ in range(100000000):
        i +=1
    return True

def main1():
    start_time=time.time()
    for tid in range(2):
        t=Thread(target=my_counter)
        t.start()
        t.join()
    end_time=time.time()
    print('单线程用时%d'%(end_time-start_time))

def main2():
    thread_array={}
    start_time=time.time()

    for tid in range(2):
        t=Thread(target=my_counter)
        t.start()
        thread_array[tid]=t
    for i in range(2):
        thread_array[i].join()
    end_time=time.time()

    print('多线程用时%d'%(end_time-start_time))

if __name__ == '__main__':
    # main1()
    main2()
