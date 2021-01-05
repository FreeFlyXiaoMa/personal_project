#!/usr/bin/env python   # -*- coding: utf-8 -*-
# @Author  : Ma
# @Time    : 2020/12/28 21:50
# @File    : test2.py
dic_={'a':50,'z':12,'b':20}
re=sorted(dic_,key=dic_.keys)
print('re:',re)


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        sentinel = ListNode(-1)
        sentinel.next = head
        Hash = {}
        prev, cur = sentinel, head
        while cur:
            if Hash.get(cur.val, -1) == 1:
                prev.next = cur.next
            else:
                Hash[cur.val] = 1
                prev = cur
            cur = cur.next
        return sentinel.next


class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        cur = head
        n = 0
        while cur.next:
            n += 1
            cur = cur.next
        c,cur2 = 0,head
        while c <= n-k:
            c += 1
            cur2 = cur2.next
        return cur2.val

# auto              // 自动检测系统环境以及编译相关的脚本
    # cc            // 关于编译器相关的编译选项的检测脚本
    # lib           // nginx编译需要的一些库的检测脚本
    # os            // 系统参数
    # types         // 数据库类型相关的辅助脚本
# conf              // 配置文件
# contrib           // 实用工具
# html              // 默认的网页文件
# man               // man手册
# src               // nginx源代码
    # core          // 核心源码
    # event         //
        # modules
    # http
        # modules
    # mail
    # misc
    # os

