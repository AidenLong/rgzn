# 元组写在小括号 () 里，元素之间用逗号隔开

tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinytuple * 2)
print(tuple + tinytuple)

# 构造包含 0 个或 1 个元素的元组比较特殊
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号

# 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
'''
注意：

1、与字符串一样，元组的元素不能修改。
2、元组也可以被索引和切片，方法一样。
3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
4、元组也可以使用+操作符进行拼接。
'''