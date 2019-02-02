'''
列表是有序的对象集合，字典是无序的对象集合。
两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。

键(key)必须使用不可变类型。

在同一个字典中，键(key)必须是唯一的。
'''

dictTmp = {}
dictTmp['one'] = "1 - 菜鸟教程"
dictTmp[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dictTmp['one'])  # 输出键为 'one' 的值
print(dictTmp[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

# 构造函数 dict() 可以直接从键值对序列中构建字典如下：
m = [('Runoob', 1), ('Google', 2), ('Taobao', 3)]
d1 = dict(m)
print(d1)

print(dict(Runoob=1, Google=2, Taobao=3))