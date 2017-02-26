#coding:utf-8

def dec(func):
    print('1 执行装饰函数外层的代码')
    def in_dec(*args):
        print('3 开始执行 in_dec,参数为',args)
        if (len(args)==0):
            return 0
        for val in args:
            if not isinstance(val, int):
                return 0

        return func(*args)

    return in_dec


@dec # 执行装饰函数外层的代码
def my_sum(*args):
    print('4 开始执行 my_sum')
    return sum(args)

def my_average(*args):
    return sum(args) / len(args)

print('2 -----------------')
# 装饰函数 是 对闭包的使用,相当于如下

# my_sum = dec(my_sum)

print(my_sum(1, 2, 3, 4))
