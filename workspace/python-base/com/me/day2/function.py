# 函数自定义和默认参数
def func(x, y=500):
    print(x, y)


func(150)
func(100, 200)
func(y=300, x=100)


# 可变参数
def func(name, *numbers):
    print(name)
    print(numbers)


func('Tom', 1, 2, 3)


# 关键字参数
def func(name, **kvs):
    print(name)
    print(kvs)


func('Jack', china='BJ', US='FSD')


# 命名关键字参数
def func(*, china, us):
    print(china, us)


func(china='BJ', us='FSD')


# 复杂情况
def func(a, b, c=0, *args, **kvs):
    print(a, b, c, args, kvs)


func(1, 2)
func(1, 2, 3)
func(1, 2, 3, 'a', 'b')
func(1, 2, 3, 'a', 'b', china='BJ', US='FSD')
func(1, 2, 3, *('a', 'b'), **({'china': 'BJ', 'US': 'FSD'}))
