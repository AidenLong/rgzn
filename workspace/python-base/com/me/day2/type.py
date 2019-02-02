
# 基本类型
import string

print(type(123))
print(type(123.12))
print(type(123.))
print(type("abc"))
print(type(None))
print(type(True))

# 容器类型
print(type([1, 2, 3, '1']))
print(type((1, 2, 3, 'abc')))
values = ['abc', 1, 2, 3.]
print(type(values[0]))
print(type(set(['a', 1, 2.])))
print(type({'a':1, 4:'bcd'}))

# 函数
def func():
    print(100)

print(type(func))

# 模块
print(type(string))

# 自定义类型与类型实例
class Cls: pass
print(type(Cls))
cls = Cls()
print(type(cls))

# 变量赋值
try:
    print(x)
except NameError:
    print('NameError: name "x" is not defined')
x = 100
x = 'abcd'