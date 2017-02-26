import os

# 要列出当前目录下的所有目录
r = [x for x in os.listdir('.') if os.path.isdir(x)]
print(r)

print('---------------')

# 列出所有的.py文件
r = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(r)