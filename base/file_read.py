#!/usr/bin/python
# coding=utf-8

import os
import demjson as JSON

filePath = './test.txt'
fileExist = os.path.exists(filePath)
if not fileExist:
    flieObject = open(filePath, "w")
    flieObject.close()
    print("create text file " + filePath)

fileObject = open(filePath, "w+")
result = JSON.encode({'number': 1})
print(result)
fileObject.write(result)
text = fileObject.read()
print("text content " + text)
fileObject.close()
