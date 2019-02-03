from collections import Iterable
from collections import Iterator

# Iterable 可迭代对象 可以使用 for 循环遍历
# Iterator 迭代器

print(isinstance([1, 2, 3], Iterable))
print(isinstance({}, Iterable))
print(isinstance(123, Iterable))
print(isinstance('aaa', Iterable))

print(isinstance([1, 2, 3], Iterator))

g = (x * x for x in range(10))
print(type(g))
print(isinstance(g, Iterable))
print(isinstance(g, Iterator))

for i in g:
    print(i)


def fib(limit):
    n, a, b = 0, 0, 1
    while n < limit:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


f = fib(6)
print(type(f))
print(isinstance(f, Iterable))
print(isinstance(f, Iterator))

for i in f:
    print(i)
