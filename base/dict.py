#!/usr/bin/python
# coding=utf-8

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'name_1', 'code': 6734, 'dept': 'sales'}

# 输出键为'one' 的值
print(dict['one'])
# 输出键为 2 的值
print(dict[2])
# 输出完整的字典
print(tinydict)
# 输出所有键
print(tinydict.keys())
# 输出所有值
print(tinydict.values())


a = {
   'x' : 1,
   'y' : 2,
   'z' : 3
}
 
b = {
   'w' : 10,
   'x' : 11,
   'y' : 2
}
 
print('Common keys:', a.keys() & b.keys())
print('Keys in a not in b:', a.keys() - b.keys())
print('Keys in a or in b',a.keys() | b.keys())
 
print('(key,value) pairs in common:', a.items() & b.items())
print('(key,value) pairs in a not in b:', a.items() - b.items())
print('(key,value) pairs in a or in b:', a.items() | b.items())