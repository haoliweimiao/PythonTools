#!/usr/bin/env python

# -*- coding: utf-8 -*-
import os

# <resources>
#    <string name="app_name">AndroidDemo</string>
# </resources>


def writeAndroidXmlHead(file):
    """
    添加android语言文本头部
    """
    file.write("<resources>")
    file.write("\n")
    file.flush()
    return


def writeAndroidXmlFoot(file):
    """
    添加android语言文本尾部
    """
    file.write("</resources>")
    file.write("\n")
    file.flush()
    return


def writeAndroidXmlContent(file, id, content):
    """
    添加android语言文本 内容
    id : string id
    content : id content
    """
    # file.write('    <string name="'+id+'">'+content+'</string>')
    content = "    <string name=\""+str(id)+"\">"+str(content)+"</string>"
    file.write(content)
    file.write("\n")
    file.flush()
    return


def createFile(fileName, mode):
    """
    创建文件
    """
    if(len(fileName) == 0 or str(fileName).isspace() == True):
        return
    file = open(fileName, mode)
    file.close()
    return


# 获取当前python文件所属文件夹路径
def getNowPath():
    # 当前文件路径
    # print(os.path.realpath(__file__))
    # 当前文件所在的目录，即父路径
    # print(os.path.split(os.path.realpath(__file__))[0])
    # 找到父路径下的其他文件，即同级的其他文件
    # print(os.path.join(proDir,"config.ini"))
    return os.path.split(os.path.realpath(__file__))[0]


def getAndroidLanguageXMLInfo(xmlPath):
    info = {}
    xmlPath = str(xmlPath)
    if(len(xmlPath) == 0 or xmlPath.isspace()):
        return info
    # xml name : C:\xxx\ZKCardAndMcuDemo-Ch-2021-02-17.xml
    # mode language year month day
    xmlPathSplit = xmlPath.split("\\")
    if(len(xmlPathSplit) == 0):
        return info
    xmlName = str(xmlPathSplit[(len(xmlPathSplit)-1)])
    print("xml name : {0}".format(xmlName))
    xmlName = xmlName.replace(".xml", "")
    xmlNameSplit = xmlName.split("-")
    if(len(xmlNameSplit) != 5):
        return info
    
    for name in xmlNameSplit:
        print("split name : {0}".format(name))
    return info

# 会死循环
# def searchFile(filePath, fileExt):
#     """
#     filePath : 文件路径
#     fileExt  : 文件后缀，用于过滤
#     """
#     fileExt=str(fileExt)
#     files = []
#     # root 当前目录路径
#     # dirs 当前路径下所有子目录
#     # files 当前路径下所有非目录子文件
#     for root, dirs, files in os.walk(filePath):
#         for file in files:
#             if os.path.splitext(file)[1] == fileExt:
#             # if str(file).endswith(fileExt):
#                 files.append(os.path.join(root, file))
#     return files


def searchFile(searchPath, fileNames, fileExt):
    for file in os.listdir(searchPath):
        filePath = os.path.join(searchPath, file)
        if os.path.isdir(filePath):
            searchFile(filePath, fileNames, fileExt)
        elif os.path.splitext(filePath)[1] == fileExt:
            # elif str(file).endswith(fileExt):
            fileNames.append(filePath)


if __name__ == "__main__":
    print(getNowPath())
    files = []
    searchFile(getNowPath(), files, ".xml")
    for file in files:
        print("find .xml file name:{0}".format(file))
