li = list(range(10))
print(li)

# 切片 [start:end:steps] >= start & < end
print(li[2:5])
print(li[:4])
print(li[5:])
print(li[0:20:3])

# 负值怎么处理？
print(li[5:-2])
print(li[9:0:-1])
print(li[9::-1])
print(li[::-2])

# 切片生成一个新的对象，原对象不变
print(li)

# list 反转
re_li = li[::-1]
print(re_li)

