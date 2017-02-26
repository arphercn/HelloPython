#coding:utf-8

# def my_sum(*args):
#     return sum(args)

# def my_average(*args):
#     return sum(args)/len(args)

# print(my_sum(1, 2, 3, 4))
# print(my_average(1, 2, 3, 4))


# def my_sum(*args):
#     if (len(args)==0):
#         return 0
#     for val in args:
#         if not isinstance(val, int):
#             return 0

#     return sum(args)

# def my_average(*args):
#     if (len(args)==0):
#         return 0
#     for val in args:
#         if not isinstance(val, int):
#             return 0

#     return sum(args)/len(args)

# print(my_sum(1, 2, 3, '2'))
# print(my_average())


def my_sum(*args):
    print('开始执行 my_sum')
    return sum(args)

def my_average(*args):
    return sum(args)/len(args)

def dec(func):
    def in_dec(*args):
        print('开始执行 in_dec,参数为',args)
        if (len(args)==0):
            return 0
        for val in args:
            if not isinstance(val, int):
                return 0

        return func(*args)

    return in_dec

my_sum = dec(my_sum)
print(my_sum(1, 2, 3, 4))
