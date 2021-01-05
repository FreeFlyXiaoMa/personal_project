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



print('===='*30)
print(100 * False > -1)
print(dir('nan'))

print('****'*20)
class A():
    def a(self):
        print('a')
class B():
    def b(self):
        print('b')
class C():
    def c(self):
        print('c')

class D(A,C):
    def d(self):
        print('d')
d=D()
d.a()
# d.b()
d.d()
print('****'*20)

# number=int(input('输入：'))
# print('number:',number)
print('===hello===')

print('****'*20)

def count():
    fs=[]
    for i in range(1,4):
        def f(a=i):
            return i*a
        fs.append(f)
    return fs
f1,f2,f3=count()
print(f1())
print(f2())
print(f3())
print('****'*20)
a=0.1
b=0.2
c=0.3
# assert  a+b==c
print('assert成功')


print('****'*20)
from functools import reduce
def func(a,b):
    return a+b

print(reduce(func,[0,1,2,3],4))

print('****'*20)
# class hello():
#     def showinfo(self):
#         print(self.x)
# hello().showinfo()

print('****'*20)
slice_list=[0,1,2,3,4,5,6,7,8]
a=slice_list[:-1]
print('a:',a)
b=slice_list[-1:]
print('b:',b)
c=slice_list[10:]
print('c:',c)
d=a+b+c
print(d)

print('****'*20)
str1='Runoob example...wow!!!'
str2='exam'
print(str1.find(str2,5))

print('****'*20)
import re
re_pattern=re.compile(r'ab.*?c')
re_match=re_pattern.match('abcfcaxc')
result=re_match.group()
print('result:',result)

print('****'*20)
def func(a):
    b=yield a
    c=yield a+b
my_func_1=func(12)
x=next(my_func_1)
y=my_func_1.send(13)
print('x:',x)
print('y:',y)

# str.find()

print('###'*20)
print(int(1.63))
print('###'*20)

print('Hello' > 'hello')

def func():
    return  [lambda x:i*x for i in range(4)]
print([m(3) for m in func()])

print('###'*20)
from inspect import isfunction
from functools import reduce

def function_wrap(param=None):
    temp_list=[i for i in range(4)]
    def inner(*args):
        if isfunction(args[0]):
            return args[0]
        else:
            return param(temp_list)
    return inner

@function_wrap
def func(para):
    if isinstance(para,list):
        return reduce(lambda x,y:x+y,para)
print(func([2,3,6,8]))
print('###'*20)

class Stu():
    name='nantian'
    def __init__(self,name):
        self.name=name

    @property
    def rename(self):
        return self.name

    @rename.setter
    def rename(self,value):
        self.name =value
obj=Stu('soft')
obj.rename='ware'
print(Stu.name)
print('###'*20)


print(callable(len))

dic3={(1,2,3):''}
print(dic3)
print('---'*30)
m=[1,2,3,4]
m.reverse()
print('m:',m)


matrix=[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
m=len(matrix)
for i in range(m):
    for j in range(1,m):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
# 对角变换后，每一行反转过来
for k in range(m):
    matrix[k].reverse()
print('matrix:',matrix)

print('---'*30)
print('---'*30)
print('---'*30)

dic_={'a':50,'z':12,'b':20}
re=sorted(dic_,key=dic_.values)
print('re:')