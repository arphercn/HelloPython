# encoding:UTF-8

# Requests 官网 http://docs.python-requests.org/en/latest/
# BeautifulSoup 官网 http://www.crummy.com/software/BeautifulSoup/

import requests
from bs4 import BeautifulSoup

response = requests.get("http://jecvay.com")
soup = BeautifulSoup(response.text, 'html.parser')

print(soup.title.text)
# print(soup.body.text)
# print(soup.p)

# for x in soup.findAll("a"):
#     print(x['href'])

for x in soup.findAll("h5"):
    print(x.text)


# 重访知乎
response2 = requests.get("http://www.baidu.com")
print(response2.headers['content-type'])
print(response2.encoding)

response2.encoding = 'utf-8'
print(response2.encoding)
soup2 = BeautifulSoup(response2.text, 'html.parser')
tag = soup2.input

print(tag.prettify())
# print(tag.select('input.bg'))
print(tag.select('input[type="submit"]'))
