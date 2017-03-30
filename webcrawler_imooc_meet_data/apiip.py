#!/usr/bin/env python
# -*- coding:utf-8 -*-

from urllib.request import urlopen
import json

ip = "117.25.13.123"
resp = urlopen("http://test.ip138.com/query/?ip=%s" % ip)
# 使用json解析获得的结果
jsonData = json.loads(resp.read().decode("utf-8"))
# 得到json里面的IP
print(jsonData.get("ip"))
