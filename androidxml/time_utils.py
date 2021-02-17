#!/usr/bin/env python

import time
import datetime


def test():

    # 格式化成2016-03-20 11:45:39形式
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    # 格式化成Sat Mar 28 22:24:24 2016形式
    print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

    # 将格式字符串转换为时间戳
    a = "Sat Mar 28 22:24:24 2016"
    print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))
    return


def getTimeFileName():
    fileName = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    return fileName


def getTodayTimeFileName():
    fileName = time.strftime("%Y-%m-%d", time.localtime())
    return fileName


def string2Date(dateStr, dateFormat):
    dateTime = datetime.datetime.strptime(dateStr, dateFormat)
    return dateTime


def date2String(date, dateFormat):
    return date.strftime(dateFormat)


def dateTime2Timestamp(date):
    return time.mktime(date.timetuple())


def timestamp2String(timestamp, timeFormat):
    return time.strftime(timeFormat, time.localtime(timestamp))


if __name__ == "__main__":
    test()
