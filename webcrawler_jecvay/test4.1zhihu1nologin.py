# encoding:UTF-8
import urllib.request
import gzip
import re
import http.cookiejar

url = "http://www.zhihu.com"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
# print(data)

def ungzip(data):
    try:        # 尝试解压
        print('正在解压.....')
        data = gzip.decompress(data)
        print('解压完毕!')
    except:
        print('未经压缩, 无需解压')
    return data

data = ungzip(data)
# print(data)

def getXSRF(data):
    cer = re.compile('name="_xsrf" value="(.*)"', flags = 0)
    # cer = re.compile('"_xsrf" = "(.*)"', flags = 0)
    strlist = cer.findall(data)
    return strlist[0]

data = getXSRF(data)
print(data)

