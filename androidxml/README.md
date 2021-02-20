# README

## 语言xml文件转Excel

运行脚本 xml2execl.py 即可，需要注意以下事项：

### xml命名规则
***xml必须是android语言xml文件***
[模块]-[语言英文简称]-[创建日期].xml
例如:
ZKCardAndMcuDemo-Ch-2021-02-17.xml

## Excel转语言xml文件
+ 每个sheet属于不同的模块
+ 列索引必须包含StringID，对应android.xml的name字段
+ 列索引剩余字段为各个语言的英文缩写