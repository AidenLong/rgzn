from functools import reduce

l = [1, 2, 3, 4]
print(reduce(lambda x, y: x + y, l))  # 这里代表着，把list中的值，一个个放进lamda的x,y中
print(reduce(lambda x, y: x + y, l, 10))  # 这样，x开始的时候被赋值为10，然后依次

new_list = list(map(lambda x: x + 1, l))  # 对数组进行处理生成新的数组
print(new_list)

l2 = [4, 5, 6, 7]
print(list(map(lambda x, y: x + y, l, l2)))  # 对两个数组处理生成新的数组

l = [100, 20, 24, 50, 110]
new = list(filter(lambda x: x < 50, l))     # 过滤
print(new)
