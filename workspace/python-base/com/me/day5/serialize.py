import pickle

# 此处定义一个dict字典对象
d = dict(name='思聪', age=29, score=80)
str = pickle.dumps(d)  # 调用pickle的dumps函数进行序列化处理
print(str)

with open('dump.txt', 'wb') as f:
    pickle.dump(d, f)   # 将内容序列化写入到file文件中


with open('dump.txt', 'rb') as f:
    d = pickle.load(f)  # 加载反序列化文件
    print(d)
    print('name is %s' % d['name'])
