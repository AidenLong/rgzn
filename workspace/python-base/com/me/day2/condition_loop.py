
# if判断
a = 100
b = 200
c = 300

if a == b:
    print(b)
elif a == c:
    print(c)
else:
    print(a)

# None判断
x = None    # false
if x is None:
    print('None')
else:
    print('not None')

# for 循环
s = 0
for i in range(0, 101):
    s += i
print(s)

# while 循环
s = 0
i = 0
while i <= 100:
    s += i
    i += 1
print(s)

# continue/pass/break
for i in range(0, 100):
    if i < 10:
        pass
    elif i < 20:
        continue
    elif i < 30:
        print(i)
    else:
        break
