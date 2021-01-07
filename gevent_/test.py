#!/usr/bin/env python   # -*- coding: utf-8 -*-
# @Author  : Ma
# @Time    : 2021/1/7 18:27
# @File    : test.py

from functools import reduce
from gevent import monkey
import datetime

monkey.patch_all()
import gevent
import requests

def task(url,results):
    """
    任务
    :param url:
    :param results:
    :return:
    """
    start=datetime.datetime.now()
    resp=requests.get(url)
    end=datetime.datetime.now()
    results.append((end-start).microseconds/1000)
while True:
    # 等待多个协程全部返回，使用joinall
    results=[]
    tasks=[]
    for i in range(50):
        url='http://39.106.115.202:5000/'
        # url='https://ts.aicc1688.com/#/pc'
        tasks.append(gevent.spawn(task,url,results))
    print('开始并发：')
    gevent.joinall(tasks)
    print('响应数量：',len(results))
    print('最小：%d,最大：%d'%(min(results),max(results)))
    print('---'*20)
