# 去除空格
s = '   abc  de  '
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s)

# 字符串连接
print('abc_' + 'defg')
s = 'abcdefg'
s += '\nlll'
print(s)

# 大小写
s = 'abc def'
print(s.upper())
print(s.upper().lower())
print(s.capitalize())

# 位置和比较
s_1 = 'abcdef'
s_2 = 'abdefg'
print(s_1.index('bcd'))
try:
    print(s_2.index('bcd'))
except ValueError:
    print('ValueError: substring is not found')
# cmp 函数被python3移除了
print(s_1 == s_2)
print(s_1 < s_2)
print(s_1 > s_2)

# 分割和连接
s = 'a,b,c,d'
print(s.split(','))
list2 = s.split(',')
print('-'.join(list2))

# 常用判断
s = 'abcdef'
print(s.startswith('ab'))
print(s.endswith('ef'))
print('abcd12'.isalnum())
print('\tabcd12'.isalnum())
print('abc'.isalpha())
print('abc123'.isalpha())
print('   '.isspace())
print('aaa111'.islower())
print('111AA'.isupper())
print('Avv Bdd'.istitle())

# 数字到字符串
print(str(5))
print(str(5.))
print(str(-5.23))

# 字符串到数字
print(int('122'))
print(int('122', 8))
print(float('-122.23'))

# 字符串到list
s = 'aaa111'
print(list(s))

# 格式化字符串
print('Hello %s!' % 'world')
print('%d-%.2f-%s' % (4, -2.3, 'hello'))