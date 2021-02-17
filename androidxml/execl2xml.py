#!/usr/bin/env python

# 引用当前路径文件
import sys
sys.path.append("./")

from androidxml.constant import ANDROID_XML_LANGUAGE_ENGLISH, COLUMN_TYPE_ID, COLUMN_TYPE_STRING_ID
from androidxml.time_utils import getTodayTimeFileName
from androidxml.file_utils import createFile
from androidxml.file_utils import writeAndroidXmlFoot
from androidxml.file_utils import writeAndroidXmlContent
from androidxml.file_utils import writeAndroidXmlHead
from androidxml.file_utils import getNowPath
from pandas.core.frame import DataFrame
import pandas as pd
import numpy as np


# xlsx根路径，生成的xml文件也存放在此
mBaseFilePath = getNowPath()
mLanguageFile = mBaseFilePath + r"\EDK显示文言1.xlsx"

def excel2xml():
    df = pd.read_excel(mLanguageFile, sheet_name=None)
    for sheetName in df.keys():
        print(sheetName)
        sheet2xml(sheetName)
    # excel=pd.ExcelFile(mLanguageFile)
    # print(excel.sheet_names)
    return


def sheet2xml(sheetName):
    df = pd.read_excel(mLanguageFile, sheet_name=sheetName)
    print("start print sheet " + sheetName)
    # 获取列数
    colNum = df.columns.size
    print(df.columns)
    # 获取行数
    rowNum = df.index.size

    # iloc[row, columns]
    colPos = 0
    rowPos = 0
    while colPos < colNum:
        languageName = df.columns[colPos]
        if(languageName == COLUMN_TYPE_ID or languageName == COLUMN_TYPE_STRING_ID):
            colPos = colPos + 1
            continue
        fileName = buildLanguageXMLName(sheetName, languageName)
        filePath = mBaseFilePath+"\\"+fileName
        print("filePath " + filePath)
        # 
        file = open(filePath, "w+")
        writeAndroidXmlHead(file)

        while rowPos < rowNum:
            rowContent = str(df.iloc[[rowPos], [colPos]].to_numpy()[0][0])
            rowID = str(df.iloc[[rowPos], [1]].to_numpy()[0][0])
            print("colPos " + str(colPos) + " rowPos " +
                  str(rowPos)+" "+rowID+" "+rowContent)
            writeAndroidXmlContent(file, rowID, rowContent)
            rowPos = rowPos + 1
        writeAndroidXmlFoot(file)
        file.flush()
        file.close()
        colPos = colPos + 1
        rowPos = 0

    return


def buildLanguageXMLName(sheetName, language):
    time = getTodayTimeFileName()
    name = sheetName + "-" + language + "-" + time + ".xml"
    return name


def test():
    excelReader = pd.ExcelFile(mLanguageFile, engine='openpyxl')  # 指定文件
    sheetNames = excelReader.sheet_names  # 读取文件的所有表单名，得到列表
    # 读取表单的内容，i是表单名的索引，等价于pd.read_excel('文件.xlsx', sheet_name=sheet_names[i])

    for sheetName in sheetNames:
        df = excelReader.parse(sheet_name=sheetName)
        changeIndex = str(COLUMN_TYPE_STRING_ID)
        # df.loc[df[changeIndex]=='year',ANDROID_XML_LANGUAGE_ENGLISH] 查询 StringID == year，竖索引为En的数据
        # tolist 将 series数据转换成list
        queryData = df.loc[df[changeIndex] == 'year', ANDROID_XML_LANGUAGE_ENGLISH].tolist()
        print(queryData)
        for data in queryData:
            print(data)

        if len(queryData):
            print(queryData[0])
        # print(df[(df.StringID == 'year')])
        # print(df.loc[0,ANDROID_XML_LANGUAGE_ENGLISH])
        # df[ANDROID_XML_LANGUAGE_ENGLISH][df['字段']
        #          == 'enroll_clear'] = "Reset modify modify"
        # df.__getitem__(ANDROID_XML_LANGUAGE_ENGLISH).__setitem__('')
        # DataFrame(df).to_excel(mLanguageFile,
        #                        sheet_name=None, index=False, header=True)
    return

def createFile():
    print(getNowPath())
    newFile = getNowPath() + r'/test.txt'
    createFile(newFile)


if __name__ == "__main__":
    excel2xml()
    # test()
