#!/usr/bin/python3

counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "runoob"  # 字符串

print(counter)
print(miles)
print(name)

# 多变量赋值
# a = b = c = 1

a, b, c = 1, 2, "runoob"

'''
标准数据类型：6个
Number  数字
String  字符串
List    列表
Tuple   元祖
Set     集合
Dictionary  字典

不可变数据（3）：Number（数字）、String（字符串）、Tuple（元组）
可变数据（3）：List（列表）、Set（集合）、Dictionary（字典）
'''

# Number（数字）
n = 111
print(isinstance(n, int))

# 判断变量类型 用 isinstance 还可以用 type
# type() 不会认为子类是一种父类类型
# isinstance()  会认为子类是一种父类类型

'''
1、Python可以同时为多个变量赋值，如a, b = 1, 2。
2、一个变量可以通过赋值指向不同类型的对象。
3、数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
4、在混合计算时，Python会把整型转换成为浮点数。'''

n1, n2 = 5.1, 6.8
print(n1 + n2)  # 加法
print(n2 - n1)  # 减法
print(n1 * n2)  # 乘法
print(n1 / n2)  # 除法，得到一个浮点数
print(n1 // n2) # 除法，得到一个整数
print(n1 % n2)  # 取余
print(n1 ** n2) # 乘方

