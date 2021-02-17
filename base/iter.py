#!/usr/bin/python
# coding=utf-8

import sys  # 引入 sys 模块

list = [1, 2, 3, 4]
it = iter(list)

# 循环
# for i in it:
#     print(i)

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()