"""
@desc: 快手
@author: ShaoLay
@email: shaoleei@126.com
@file: kuaishou.py
@time: 2021/08/02 下午12:37
@environment: PyCharm
"""
# -*-coding:utf-8-*-
import uiautomator2 as u2
import time


# 连接手机
d = u2.connect()


def sign_in():
    """签到领金币"""
    d.click(0.636, 0.97)


def click_index():
    """点击首页"""
    d.click(0.636, 0.97)


def click_money():
    """点击去赚钱按钮"""
    d.click(0.632, 0.974)


def ad():
    """看广告"""
    d.click(0.622, 0.975)   # 点击赚钱按钮
    d.swipe_ext("up", 0.6)

    i = 0
    while i < 20:
        d.click(0.822, 0.516)
        time.sleep(40)          # 停顿40秒
        d.click(0.08, 0.073)    # 关闭广告
        i = i + 1               # 再次循环


def chest():
    """开宝箱"""
    d.click(0.809, 0.869)


def index():
    """
    首页刷视频金币
    :return:
    """
    d(resourceId="android:id/text1", text="首页").click()
    while True:
        i = 0
        while i < 100:
            time.sleep(20)              # 停顿20秒
            d.swipe_ext("up", 1)        # 滑动视频
            i = i + 1
            print("第" + str(i) + "次翻页")

        click_money()
        time.sleep(10)
        chest()
        time.sleep(2)


def live():
    """直播间领金币"""
    i = 0
    while i < 10:
        d.click(0.632, 0.974)
        d.swipe_ext("up", 1)
        d.swipe_ext("up", 0.2)
        d.click(0.849, 0.732)
        time.sleep(60)
        d.swipe_ext("up", 1)


if __name__ == '__main__':
    # click_money()
    # click_index()
    # click_money()
    # live()
    # ad()

    index()
