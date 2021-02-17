#!/usr/bin/env python

# 引用当前路径文件
import sys
sys.path.append("./")

from androidxml.file_utils import getAndroidLanguageXMLInfo, getNowPath, searchFile
import xml.dom.minidom
import csv


def test():
    filePath = r"C:\Users\Von\work\workspace\python\pandas_demo\ZKCardAndMcuDemo-中文-2021-02-14-12-43-01.xml"
    # 打开xml文档
    dom = xml.dom.minidom.parse(filePath)
    # 获取根元素
    root = dom.documentElement
    # 获取string列表
    resource = root.getElementsByTagName('string')
    category = 'en_string'
    for node in resource:
        # 得到名称
        key = node.getAttribute('name')
        # 得到对应的值
        value = node.firstChild.data
        data = {}
        data['name'] = key
        data['value'] = value
        print("name "+key+"\nvalue "+value+"\n")
        # 写到表格
        # with open('{}.csv'.format(category), 'a', encoding='utf_8_sig', newline='') as f:
        #     w = csv.writer(f)
        #     w.writerow(data.values())

    return

def xml2excel():
    files = []
    searchFile(getNowPath(), files, ".xml")
    for file in files:
        print("start read android language xml file: {0}".format(file))
        getAndroidLanguageXMLInfo(file)
    return


if __name__ == "__main__":
    # test()
    xml2excel()
