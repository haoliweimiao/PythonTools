#!/usr/bin/env python

# 表格列索引特殊字段名称
# ID
COLUMN_TYPE_ID = "ID"
# String ID, 对应android language xml中的name
COLUMN_TYPE_STRING_ID = "StringID"


# 语言
# 英文
ANDROID_XML_LANGUAGE_ENGLISH = "En"
# 中文
ANDROID_XML_LANGUAGE_CHINESE = "Ch"

# 解析android xml 文件获取相应的信息
# 模块名称
ANDROID_XML_LANGUAGE_INFO_MODEL_NAME = "info_model_name"
# 生成xml时间（xml to excel 文件对应时间）
ANDROID_XML_LANGUAGE_INFO_TIME = "info_time"
# xml语言类型
ANDROID_XML_LANGUAGE_INFO_LANGUAGE = "info_language"
# android xml 文件绝对路径
ANDROID_XML_LANGUAGE_INFO_XML_PATH = "info_xml_path"
# 模块下的语言种类集合
ANDROID_XML_LANGUAGE_INFO_MODEL_LANGUAGES = "info_model_languages"
# 模块下的语言 从xml依据string id 读取出来的缓存
ANDROID_XML_LANGUAGE_INFO_MODEL_LANGUAGE_CACHE_DATA = "info_model_language_cache_data"