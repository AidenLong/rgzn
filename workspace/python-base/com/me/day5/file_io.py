# utf-8

file = open("Test.java")

line = file.readline()
while line:
    print(line)
    line = file.readline()

file.close()

print("======2======")
for i in open('Test.java'):
    print(i)

print("======3======")
with open('Test.java') as f:
    for i in f:
        print(i)