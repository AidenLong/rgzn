# 推导
li = []
for i in range(20):
    if (i % 2) == 0:
        li.append(i)
print(li)

li = [1] * 10
li[3] = 3
print(li)
li = [i * 2 for i in range(10)]
print(li)

'''
li_2d = [[0] * 3] * 3
print(li_2d)
 软复制，复制的是引用，00修改时，10,20跟着修改
li_2d[0][0] = 100
print(li_2d)
'''

li_2d = [[0] * 3 for i in range(3)]
li_2d[0][0] = 100
print(li_2d)

# 推导生成set和dict
s = {x for x in range(10) if x % 2 == 0}
print(s)
d = {x: x % 2 == 0 for x in range(10)}
print(d)
