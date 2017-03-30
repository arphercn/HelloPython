# encoding:UTF-8
import urllib.request

url = "http://baidu.com"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
print(data)

a = urllib.request.urlopen(url)

b = type(a)
print(b)

b = a.geturl()
print(b)

b = a.info()
print(b)

b = a.getcode()
print(b)