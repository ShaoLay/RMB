"""
@desc:
@author: ShaoLay
@email: shaoleei@126.com
@file: run.py
@time: 2021/08/02 下午12:37
@envirmonent: PyCharm
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


def ad():
    """看广告"""
    d.click(0.622, 0.975)
    d.swipe_ext("up", 1)
    i = 0
    while(i < 20):
        d.click(0.869, 0.803)
        time.sleep(40)
        d.click(0.08, 0.073)
        i = i + 1


def index():
    """
    首页刷视频金币
    :return:
    """
    d(resourceId="android:id/text1", text="首页").click()
    time.sleep(20)              # 停顿20秒
    d.swipe_ext("up", 1)        # 滑动视频

# 每隔20分钟点击宝箱
if __name__ == '__main__':
    pass