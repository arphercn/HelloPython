# closure: 内部函数对enclosing作用域的变量进行引用

scoreline = 60

# def func(val):
#     if (val>scoreline):
#         print('pass')
#     else:
#         print('failed')

#     def in_func():
#         print(val)

#     in_func()

# func(89)


# scoreline = 60

# def func(val):
#     if (val>scoreline):
#         print('pass')
#     else:
#         print('failed')

#     def in_func():
#         print(val)

#     # in_func()
#     return in_func # 注意没有()

# f = func(99)

# f() # 调用的是in_func()


scoreline = 'ok'

def func(val):
    print('%x' %id (val))
    if (val==scoreline):
        print('pass')
    else:
        print('failed')

    def in_func():
        print(val)

    return in_func

f = func('ok')

f()
print(f.__closure__)

