#!/usr/bin/env python
# -*- coding:utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql.cursors

resp = urlopen("http://baike.baidu.com/link?url=RhIheyeqbK3Smotxuhzf3EwhWEdrM16s3uLck3YTt94RbIHG44vgFxoFQOOKwXtxkA949wI8wx7tnUNAzpA65q").read().decode("utf-8")

soup = BeautifulSoup(resp, "html.parser")

listUrls = soup.findAll("a", href=re.compile("^/view/"))

try:
    conn = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='test_python',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    for url in listUrls:
        if not re.search("\.(jpg|JPG)$", url["href"]):

            with conn.cursor() as cursor:

                sql = "INSERT INTO `urls` (`name`, `url`) VALUES (%s, %s)"
                cursor.execute(sql, (url.get_text(), url["href"]))

            conn.commit()


    with conn.cursor() as cursor:

        sql = "SELECT `name`, `url` FROM `urls` where `id` is not null"
        cursor.execute(sql)
        data = cursor.fetchall()
        i = 1
        for d in data:
            # 注意int类型需要使用str函数转义str(d['id'])
            print("ID:" + str(i) + '  名称：' + d['name'] + "  网站：www.baike.com" + d['url'])
            i = i + 1

    conn.close()

except  Exception :print("操作数据库发生异常")