d = {'a': 1, 'b': 2, 1: 'one', 2: 'two'}
print(type(dict))
print(type(d))
print(d)

# 访问元素
print(d['a'])
print(d[1])

# 判断key是否存在
print('a' in d)
print(2 in d)

# 添加元素
d.update({3: 'three'})
print(d)

# 删除元素
del(d[3])
print(d)

# 遍历
for key in d:
    print(d[key], end="\t")
print(".........")
for k, v in d.items():
    print(k, v, end="\t")
print(".........")

keys = d.keys()
print(type(keys))
print(keys)
