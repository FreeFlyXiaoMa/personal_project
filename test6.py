#!/usr/bin/env python   # -*- coding: utf-8 -*-
# @Author  : Ma
# @Time    : 2021/1/5 17:58
# @File    : test6.py

class Apple():
    def __repr__(self):
        return "苹果"


class Banana():
    def __repr__(self):
        return "香蕉"


class SimpleFactory():

    @staticmethod
    def get_gruit(name):
        if name == 'a':
            return Apple()
        elif name == 'b':
            return Banana()

re=SimpleFactory().get_gruit('a')
print(re)