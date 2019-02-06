import traceback

try:
    r = 10 / 0
except ZeroDivisionError as e:
    print(e)
    r = 1
else:
    print('没有异常')
finally:
    print('finally')
print(r)
