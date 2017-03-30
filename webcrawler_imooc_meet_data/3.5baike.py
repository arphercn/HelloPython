#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 引入开发包
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# 请求URL并把结果用UTF-8编码
resp = urlopen("http://baike.baidu.com/link?url=RhIheyeqbK3Smotxuhzf3EwhWEdrM16s3uLck3YTt94RbIHG44vgFxoFQOOKwXtxkA949wI8wx7tnUNAzpA65q").read().decode("utf-8")

# 使用BeautifulSoup去解析
soup = BeautifulSoup(resp, "html.parser")

# 获取所有以/wiew/开头的a标签的href属性
listUrls = soup.findAll("a", href=re.compile("^/view/"))

# 输出所有的词条对应的名称和URL
for url in listUrls:
    # 过滤一.jpg或.JPG结尾的URL
    if not re.search("\.(jpg|JPG)$", url["href"]):
        # 输出URL的文字和对应的链接
        # string 只能获取一个 get_text() 获取标签下所有的文字
        print(url.get_text(), " ----> ", "http://baike.baidu.com" + url["href"])
