li = [1, 2, '345', [1, 2, 3], {1: 'one', 2: 'tow'}]
print(type(li))
print(type(list))

# 元素访问
print(li[0])
print(li[-1])
print(li[-2])

# 查找元素位置
print(li.index(1))
print(li.index('345'))

# 添加元素
l_a = [1, 2]
l_a.append(3)
l_a.append(4)
l_b = [4, 5]
l_a.extend(l_b)
print(l_a)

# 判断是否为空
l_a = []
if not l_a:
    print('Empty')  # not xx 和 xx is None 不是一回事
if len(l_a) == 0:
    print('Empty')

# 遍历元素
for i in li:
    print(i)
for i in range(len(li)):
    print(li[i])

# 删除元素
del(li[1])
print(li)

# tuple
t = (1, 2, 3, '456')
print(type(t))
# tuple 不允许修改

