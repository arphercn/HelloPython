#!/usr/bin/env python
# -*- coding:utf-8 -*-

from urllib.request import urlopen

html = urlopen("https://en.wikipedia.org/robots.txt")

print(html.read().decode("utf-8"))
