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
        time.sleep(8)
        i = i + 1
        print("第 " + str(i) + " 次翻页！")


def chest():
    """
    开宝箱
    """
    pass


def read():
    """
    阅读小说
    """
    while True:
        time.sleep(15)
        d.swipe_ext("left", 0.6)


def ad():
    """看广告"""
    d.click(0.504, 0.96)    # 点击去赚钱

    d.click(0.806, 0.5)     # 播放广告按钮
    time.sleep(40)
    d.click(0.911, 0.052)   # 点击关闭广告按钮
    d.click(0.487, 0.637)   # 坚持退出按钮


if __name__ == '__main__':
    read()
