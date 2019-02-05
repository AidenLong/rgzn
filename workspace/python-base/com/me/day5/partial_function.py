import functools

print(int('12312'))
print(int('12312', base=8))
print(int('12312', base=16))


def int2(x, base=2):
    return int(x, base)


print(int2('1010'))

int2 = functools.partial(int, base=2)
print(int2('1111'))

kw = {'base': 2}
int2 = functools.partial(int, **kw)
print(int2('1111'))

max2 = functools.partial(max, 10)
args = (10, 5, 6, 7)
print(max2(*args))
