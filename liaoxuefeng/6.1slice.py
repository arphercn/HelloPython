#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 打印 1, 3, 5 ... 15
odds = []
i = 1
while i <= 15:
    odds.append(i)
    i = i+2
print(odds)

# 打印list的前3个
names = ['Jim', 'John', 'Lucy', 'Lily', 'Lilei']
namesson = []
num = 3
for i in range(num):
    namesson.append(names[i])
print(namesson)

# print(names[0:3])
# print(names[:3])
# print(names[1:3])
# print(names[-2:])
print(names[-2:-1])

nums = list(range(100))
# print(nums)
print(nums[:10])
print(nums[-10:])
print(nums[:10:2])
print(nums[::10])
