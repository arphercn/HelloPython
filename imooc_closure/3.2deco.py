#coding:utf-8

def deco(func):
    def in_deco(x, y):
        print('执行装饰代码,检查传入的参数')
        func(x, y)

    return in_deco

@deco
def bar(x, y):
    print('执行bar函数:x+y=',x+y)

bar(1, 2)