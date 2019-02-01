#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# int
import sys

i, b = 1, 2
print(i + b)
print('------------------------------')

# bool
flag = True
print(flag)
print('------------------------------')

# float
f1, f2 = 1.23, 3E-2
print(f1)
print(f2)
print('------------------------------')

# complex 复数
c1, c2 = 1 + 2j, 1.1 + 2.2j
print(c1)
print(c2)
print('------------------------------')

# string
s = "string"
print(s)

word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
                \t你好"""

print(word)
print(sentence)
print(paragraph)
print('------------------------------')

str = 'Runoob'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串

print('------------------------------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

# 键盘输入
inputStr = input("\n\n按下 enter 键后退出。")
print(inputStr)

# 多行代码在一行
x = 'runoob'; sys.stdout.write(x + '\n')

# print 打印
x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
print(x, end=" ")
print(y, end=" ")
