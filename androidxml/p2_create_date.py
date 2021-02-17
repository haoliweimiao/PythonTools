#!/usr/bin/env python

import numpy as np
import pandas as pd


def test():
    createSeries()
    createTimeDataFrame()
    createDataFrame()
    return
    

def createSeries():
    # 用值列表生成 Series (opens new window)时，Pandas 默认自动生成整数索引：
    s1 = pd.Series([1, 3, 5, np.nan, 6, 8])
    print("start print create series")
    print(s1)
    return


def createDateRange():
    # 生成日期时间索引
    dates = pd.date_range('20210212', periods=6)
    print("start print create date range")
    print(dates)
    return dates


def createTimeDataFrame():
    # 用含日期时间索引与标签的 NumPy 数组生成 DataFrame (opens new window)：
    dates = createDateRange()
    df = pd.DataFrame(np.random.randn(
        6, 4), index=dates, columns=list('ABCD'))
    print("start print create data frame")
    print(df)
    return df


def createDataFrame():
    df2 = pd.DataFrame({'A': 1.,
                        'B': pd.Timestamp('20130102'),
                        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                        'D': np.array([3] * 4, dtype='int32'),
                        'E': pd.Categorical(["test", "train", "test", "train"]),
                        'F': 'foo'})
    print("start print data frame")
    print(df2)
    return df2


if __name__ == "__main__":
    test()
