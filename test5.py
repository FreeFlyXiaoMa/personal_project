#!/usr/bin/env python   # -*- coding: utf-8 -*-
# @Author  : Ma
# @Time    : 2021/1/5 11:57
# @File    : test5.py

class A():
    def __init__(self):
        self.child=None
    def destroy(self):
        self.child=None

class B():
    def __init__(self):
        self.parent=None
    def destroy(self):
        self.parent=None

def test3():
    a=A()
    b=B()
    a.child=b
    b.parent=a
    a.destroy()
    b.destroy()
import weakref

def test4():
    a=A()
    b=B()
    a.child=weakref.ref(b)
    b.parent=weakref.ref(a)

import objgraph
test4()
print(objgraph.count('A'))
print(objgraph.count('B'))
print('---'*20)

import asyncio,os
from threading import current_thread

async def sum(a,b):
    print('[%s-%s] coroutine start to do:%s + %s'%(os.getpid(),current_thread().getName(),a,b))
    await asyncio.sleep(1)
    r=int(a) + int(b)
    print('[%s-%s] coroutine start to do:%s + %s=%s'%(os.getpid(),current_thread().getName(),a,b,r))
    return r

def main(a,b,c,d):
    loop=asyncio.get_event_loop()
    task=asyncio.gather(sum(a,b),sum(c,d))
    loop.run_until_complete(task)
    r1,r2=task.result()
    r=r1*r2
    print('[%s-%s] coroutine start to do:%s * %s===%s'%(os.getpid(),current_thread().getName(),r1,r2,r))
    loop.close()

import abc

if __name__=='__main__':
    main('1','2','3','4')