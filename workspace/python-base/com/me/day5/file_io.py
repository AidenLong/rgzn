# 读取文本文件
file = open("./tmp/Test.txt", 'r', encoding='utf8')

line = file.readline()
while line:
    print(line)
    line = file.readline()

file.close()

print("======2======")
for i in open('./tmp/Test.txt', encoding='utf8'):
    print(i)

print("======3======")
with open('./tmp/Test.txt', encoding='utf8') as f:
    for i in f:
        print(i)

# 复制二进制文件
with open('./tmp/高帆.jpg', 'rb') as img, open('./tmp/123.jpg', 'wb') as out_img:
    for i in img:
        out_img.write(i)
