#!/usr/bin/env python
# -*- coding:utf-8 -*-

from urllib import request

req = request.Request("http://www.baidu.com")
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36")
resp = request.urlopen(req)
resp = request.urlopen(req)

print(resp.read().decode("utf-8"))

