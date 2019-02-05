import os
import shutil

# 系统名称
print(os.name)
# 环境变量
print(os.environ)
# 当前目录的绝对路径
print(os.path.abspath("."))
# 拼出目录
print(os.path.join('D:\syl\\rgzn', 'pic'))

# 创建目录
os.mkdir('D:\\syl\\rgzn\\pic')

# 删除目录
os.rmdir('D:\\syl\\rgzn\\pic')

# 拆分路径和文件
print(os.path.split('D:\\syl\\rgzn\\pic\\123.txt'))

# 拆分到文件扩展名
print(os.path.splitext('D:\\syl\\rgzn\\pic\\123.txt'))

# 文件重命名
# os.rename('D:\\syl\\rgzn\\pic\\123.txt', '222.txt')

# 删除文件
# os.remove('D:\\syl\\rgzn\\pic\\123.txt')

# 使用第三方库执行文件复制功能
# shutil.copyfile('/path/to/file', '/path/to/other/file')

# 列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])

# 列出.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
