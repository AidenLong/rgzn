# 可以使用大括号 { } 或者 set() 函数创建集合，
# 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

print(student)

if 'Rose' in student:
    print('Rose in set')
else:
    print('Rose not in set')

a = set('12345')
b = set('45678')

print(a)
print(a - b)    # a 和 b的差集
print(a | b)    # a 和 b的并集
print(a & b)    # a 和 b的交集
print(a ^ b)    # a 和 b总不同时存在的元素