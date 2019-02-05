import json

# 定义dict字典对象
d1 = dict(name='小王', age=20, score=80)
str = json.dumps(d1)  # 调用json的dumps函数进行json序列化处理
print(str)

# 调用json的loads函数进行反序列化处理
d2 = json.loads(str)
