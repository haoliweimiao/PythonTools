#!/usr/bin/env python

import numpy as np
import pandas as pd
import p2_create_date as p2


def test():
    dfTimeData = p2.createTimeDataFrame()
    dfData = p2.createDataFrame()

    printHead(dfTimeData)
    printIndex(dfTimeData)
    printColumns(dfTimeData)

    printNumpy(dfTimeData, dfData)

    printDescribe(dfTimeData)
    printT(dfTimeData)

    printSortIndex(dfTimeData)
    printSortValues(dfTimeData)
    printQueryData(dfTimeData)
    return


def printHead(df):
    print("start print data frame head")
    print(df.head())
    return


def printIndex(df):
    print("start print data frame index")
    print(df.index)
    return


def printColumns(df):
    print("start print data frame columns")
    print(df.columns)
    return


def printNumpy(dfTimeData, dfData):
    print("start print time data numpy")
    print(dfTimeData.to_numpy())

    print("start print data numpy")
    print(dfData.to_numpy())
    return


def printDescribe(df):
    # 可以快速查看数据的统计摘要
    print("start Describe")
    print(df.describe())
    return


def printT(df):
    # 转置数据：
    print("start T")
    print(df.T)
    return


def printSortIndex(dfTimeData):
    # 按轴排序：
    print("print sort index data")
    print(dfTimeData.sort_index(axis=1, ascending=False))
    return


def printSortValues(dfTimeData):
    # 按值排序：
    print("print sort values data")
    print(dfTimeData.sort_values(by='B'))
    return

def printQueryData(dfTimeData):
    # df.loc['2021-02-15','B'] 查询 索引为 2021-02-15 B 
    # tolist 将 series数据转换成list
    queryData=dfTimeData.loc['2021-02-15','B'].tolist()
    print("print query values data")
    print(queryData)
    return

if __name__ == "__main__":
    test()
