#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time : 2021/8/6 下午10:29
# @Author : ShaoLay
# @Email : shaoleei@126.com
# @File : fanqie.py
# @Desc ：番茄小说
import uiautomator2 as u2
import time


# 连接手机
d = u2.connect()


def read():
    """
    阅读刷金币
    """
    i = 0
    while i < 100:
        d.swipe_ext("left",0.6)
        time.sleep(15)
        i = i + 1
        print("第" + i + "次翻页")


def chest():
    """
    开宝箱
    """
    pass


def video():
    """
    看广告视频刷金币，每个视频大概停留15-20秒
    """
    pass


def task():
    """
    点击任务按钮
    """
    pass


if __name__ == '__main__':
    pass
