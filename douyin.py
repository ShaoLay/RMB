#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time : 2021/8/7 下午7:36
# @Author : ShaoLay
# @Email : shaoleei@126.com
# @File : douyin.py
# @Desc ：抖音
import uiautomator2 as u2
import time


# 连接手机
d = u2.connect()


def index():
    """
    首页刷金币
    """
    d.click(0.092, 0.96)
    i = 0
    while True:
        d.swipe_ext("up", 1)
        time.sleep(20)
        i = i + 1
        print("第" + str(i) + "翻页！")


def chest():
    """
    开宝箱
    """
    pass


if __name__ == '__main__':
    index()
