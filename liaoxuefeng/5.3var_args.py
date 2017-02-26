#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#         必选参数   可变参数
def hello(greeting, *args):
    if (len(args)==0):
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting, ', '.join(args)))

hello('Hi') # => greeting='Hi', args=()
hello('Hi', 'Sarah') # => greeting='Hi', args=('Sarah')
hello('Hello', 'Michael', 'Bob', 'Adam') # => greeting='Hello', args=('Michael', 'Bob', 'Adam')

#简化调用方法 
# names 可以是列表list: names = ['Bart', 'Lisa']    
# names 可以是元组tuple: names = ['Bart', 'Lisa']
# 因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。  
names = ('Bart', 'Lisa')
hello('Hello', *names) # => greeting='Hello', args=('Bart', 'Lisa')