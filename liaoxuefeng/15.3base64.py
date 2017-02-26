# -*-coding:utf-8-*-

import base64,re

s = base64.b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.b64decode(s).decode('utf-8')
print(d)

s = base64.urlsafe_b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.urlsafe_b64decode(s).decode('utf-8')
print(d)

print('---------------')

def safe_base64_encode(s):                                     # 可以去掉==结尾的编码函数
    encode = base64.urlsafe_b64encode(s)                    #调用url safe编码方法，适用范围更广
    print('原处理后的BYTES应为: %s' % encode)
    en2str = str(encode, encoding = 'utf-8')                #将BYTES转化为STR, 才能使用正则表达式
    temp = re.match(r'^([\w\d]*)\=*$',en2str)                #正则表达式匹配分组，将有效内容和尾部补位的=进行分割
    encode = bytes(temp.group(1), encoding = 'utf-8')        #将组1的STR转回BYTES
    return encode

def safe_base64_decode(s):                                    # 可以识删除==结尾的编码函数
    temp = s + b'='*(4-len(s)%4)                            #  略
    decode = base64.urlsafe_b64decode(temp)
    return decode

target = b'abcdefg123456789'
print('目标bytes: %s' % target)
en = safe_base64_encode(target)
print('经自定编码函数处理后为: %s' % en)
de = safe_base64_decode(en)
print('经自定解码函数处理后为: %s' % de)