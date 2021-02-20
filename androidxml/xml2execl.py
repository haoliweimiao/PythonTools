#!/usr/bin/env python


import sys
sys.path.append("./")

import os
import numpy as np
import pandas as pd
from androidxml.file_utils import getAndroidLanguageXMLInfo, getNowPath, getOpenMode, searchFile
import xml.dom.minidom
import csv
from androidxml.constant import ANDROID_XML_LANGUAGE_CHINESE, ANDROID_XML_LANGUAGE_INFO_LANGUAGE, ANDROID_XML_LANGUAGE_INFO_MODEL_LANGUAGES, ANDROID_XML_LANGUAGE_INFO_MODEL_LANGUAGE_CACHE_DATA, ANDROID_XML_LANGUAGE_INFO_MODEL_NAME, ANDROID_XML_LANGUAGE_INFO_TIME, ANDROID_XML_LANGUAGE_INFO_XML_PATH, COLUMN_TYPE_ID, COLUMN_TYPE_STRING_ID
from androidxml.time_utils import getTodayTimeFileName

modelDataFrameData = {}

def checkExcelColumnIndex(excelFile, dataFrame, indexName):
    # 检测Excel列索引，不存在则新增
    indexName = str(indexName)
    if(len(indexName) == 0):
        return

    queryCount = sum(dataFrame.columns == indexName)
    if(queryCount == 0):
        # 不存在，插入索引
        dataFrame.columns.tolist().insert(queryCount, indexName)
        # DataFrame(dataFrame).to_excel(excelFile,
        #                        sheet_name=None, index=False, header=True)
    return


def xml2excel():
    # 1.获取xml语言文件
    # 2.创建excel表格(若不存在)。存在则插入内容
    # 3.遍历xml文件，依据相应的语言类型，插入相应的应用模块(对应Excel sheet)，相应的语言插入相应的列
    # 4.遍历xml中的每一项，针对name(对应Excel 中的StringID)，新增or修改相应的语言文本
    xmlFiles = []
    nowPath = getNowPath()
    searchFile(nowPath, xmlFiles, ".xml")

    androidLanguageInfos = {}

    # 将所有xml文件相应的路径、语言等信息写入到内存
    readAllXmlFileInfoToMemory(xmlFiles, androidLanguageInfos)

    # 将所有xml文件中的语言数据写入内存
    readAllXmlFileLanguageToMemory(androidLanguageInfos)

    print(androidLanguageInfos)

    print("start create excel DataFrame")
    createAllModelDataFrame(androidLanguageInfos)

    excelFilePath = nowPath + r'/AndroidLanguage-' + getTodayTimeFileName() + r'.xlsx'
    # checkExcelFileExist(excelFilePath)

    writer = pd.ExcelWriter(excelFilePath)
    print("print excel DataFrame")
    print(modelDataFrameData.keys())

    for key in modelDataFrameData.keys():
        df = modelDataFrameData[key]
        df.to_excel(writer, sheet_name=key)
    writer.save()

    return

def createAllModelDataFrame(androidLanguageInfos):
    for modelName in androidLanguageInfos.keys():
            # print("modelName : {0}".format(modelName))
            languages = androidLanguageInfos[modelName][ANDROID_XML_LANGUAGE_INFO_MODEL_LANGUAGES]
            
            modelAllLanguageData={}

            # 获取模块下所有的StringID，部分xml 内容不一致(写的代码有问题，未翻译完整)
            modelLanguageCommonKeys = {}
            for language in languages:
                data = androidLanguageInfos[modelName][language][ANDROID_XML_LANGUAGE_INFO_MODEL_LANGUAGE_CACHE_DATA]
                # print("language:{0} size:{1}".format(language, len(data)))
                # print(data)
                modelLanguageCommonKeys = modelLanguageCommonKeys | data.keys()

            # print(modelLanguageCommonKeys)

            checkDictKeyAddArray(modelAllLanguageData, COLUMN_TYPE_STRING_ID)
            for language in languages:
                checkDictKeyAddArray(modelAllLanguageData, language)

            for stringID in modelLanguageCommonKeys:
                modelAllLanguageData[COLUMN_TYPE_STRING_ID].append(stringID)
                for language in languages:
                    modelLanguageCacheData = androidLanguageInfos[modelName][language][ANDROID_XML_LANGUAGE_INFO_MODEL_LANGUAGE_CACHE_DATA]
                
                    languageData = None
                    if stringID in modelLanguageCacheData:
                        languageData = modelLanguageCacheData[stringID]
                    modelAllLanguageData[language].append(languageData)
            print("\nmodel : {0}, modelAllLanguageData:\n{1}\n".format(modelName, modelAllLanguageData))

            dataFrame = pd.DataFrame(modelAllLanguageData)
            
            # print("print data frame")
            # print(dataFrame)

            checkDictKey(modelDataFrameData, modelName)
            modelDataFrameData[modelName] = dataFrame
    return


def checkDictKey(dict, key):
    if(dict == None):
        print("checkDictKey error! dict is null")
        return

    if(key == None or len(key) == 0):
        print("checkDictKey error! key is null")
        return

    if not key in dict:
        dict[key] = {}
    return

def checkDictKeyAddArray(dict, key):
    if(dict == None):
        print("checkDictKey error! dict is null")
        return

    if(key == None or len(key) == 0):
        print("checkDictKey error! key is null")
        return

    if not key in dict:
        dict[key] = []
    return

def readAllXmlFileInfoToMemory(xmlFiles, androidLanguageInfos):
    # 将所有xml文件相应的路径、语言等信息写入到内存
    for file in xmlFiles:
        print("start read android language xml file: {0}".format(file))
        info = getAndroidLanguageXMLInfo(file)

        if(len(info) == 0):
            print("{0} is not android language xml file".format(file))
            continue

        modelName = info[ANDROID_XML_LANGUAGE_INFO_MODEL_NAME]
        language = info[ANDROID_XML_LANGUAGE_INFO_LANGUAGE]
        timeStr = info[ANDROID_XML_LANGUAGE_INFO_TIME]
        xmlPath = info[ANDROID_XML_LANGUAGE_INFO_XML_PATH]

        if not modelName in androidLanguageInfos:
            androidLanguageInfos[modelName] = {}

        androidLanguageInfos[modelName][language] = info
    return

def readAllXmlFileLanguageToMemory(androidLanguageInfos):
    for modelName in androidLanguageInfos.keys():
        print("modelName : {0}".format(modelName))
        languages = []
        for language in androidLanguageInfos[modelName].keys():
            languages.append(language)
            print("language : {0}".format(language))
            dictLanguage = androidLanguageInfos[modelName][language]
            checkDictKey(
                dictLanguage, ANDROID_XML_LANGUAGE_INFO_MODEL_LANGUAGE_CACHE_DATA)
            dictLanguageCache = dictLanguage[ANDROID_XML_LANGUAGE_INFO_MODEL_LANGUAGE_CACHE_DATA]

            xmlPath = dictLanguage[ANDROID_XML_LANGUAGE_INFO_XML_PATH]
            # 打开xml文档
            dom = xml.dom.minidom.parse(xmlPath)
            # 获取根元素
            root = dom.documentElement
            # 获取string列表
            resource = root.getElementsByTagName('string')
            for node in resource:
                # 得到名称
                key = node.getAttribute('name')
                value = ""
                if(node.firstChild != None):
                    # 得到对应的值
                    value = node.firstChild.data
                print("name " + key + "\nvalue " + value + "\n")
                # 将xml中 各个StringID + 值插入 androidLanguageInfos[modelName][language][cacheData][StringID]
                checkDictKey(dictLanguageCache, key)
                # if not key in dictLanguage:
                #     dictLanguage[key]={}

                dictLanguageCache[key] = value

        checkDictKey(androidLanguageInfos[modelName],
                     ANDROID_XML_LANGUAGE_INFO_MODEL_LANGUAGES)
        androidLanguageInfos[modelName][ANDROID_XML_LANGUAGE_INFO_MODEL_LANGUAGES] = languages
    return


def checkExcelFileExist(filePath):
    # 文件存在则不创建，不覆盖内容
    # openMode = getOpenMode(False, True, True, False, True)
    # openMode = str(openMode)
    # excelFile = open(filePath, openMode)
    # excelFile.close()

    # 需要使用以下方法创建Excel，否则无法正常打开
    if not os.path.exists(filePath):
        df = pd.DataFrame()
        df.to_excel(filePath)
    return

if __name__ == "__main__":
    xml2excel()
