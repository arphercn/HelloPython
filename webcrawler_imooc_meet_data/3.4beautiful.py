#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup as bs
import re

html_doc = """
<html><head><title>The Dormouse's story<a>Hello</a></title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://exampleScom/elsie" class="sister1" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# bs为别名
soup = bs(html_doc, "html.parser")

# 打印第一个a标签
print(soup.a)

# 格式化
print(soup.prettify())

# 打印title标签里的所有文字(不管是否包含标签),相当于JQuery的html()
print(soup.title.get_text())

# .string相当于JQuery的.text
print(soup.find(id="link2").string)

# 找出第一个
print(soup.find("a", {"class": "sister"}))

# for link in soup.findAll("a"):
#     print(link.string)


# 遍历b开头的标签
# for tag in soup.find_all(re.compile("^b")):
#     print(tag.name)
# body
# b

data = soup.findAll("a", href=re.compile(r"^http://example\.com/"))
print(data)

