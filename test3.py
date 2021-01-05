#!/usr/bin/env python   # -*- coding: utf-8 -*-
# @Author  : Ma
# @Time    : 2020/12/29 14:53
# @File    : test3.py


def commonArea(rec1,rec2):
    l_x = max(rec1[0],rec2[0])
    d_y = max(rec1[3],rec2[3])
    r_x = min(rec1[2],rec2[2])
    u_y = min(rec1[1],rec2[1])
    # print('l_x:',l_x)
    # print(d_y)
    # print(r_x)
    # print(u_y)
    length = r_x-l_x
    wide = u_y-d_y
    print('wide:',wide)
    print('length:',length)
    if length>0 and wide>0:
        return length*wide
    return 0

#rec = [x0,y0,x1,y1]
# rec1=[1,5,6,2]
# rec2=[4,4,7,1]
rec1=[1,7,10,3]
rec2=[2,6,5,0]
print(commonArea(rec1,rec2))


import time

def decorate(func):
    def wrapper(*args,**kwrags):
        start_time=time.time()
        func(*args,**kwrags)
        end_time=time.time()
        msecs=end_time-start_time
        print(msecs)
    return wrapper


@decorate
def func(a,b):
    print('resource func')

func(1,2)

