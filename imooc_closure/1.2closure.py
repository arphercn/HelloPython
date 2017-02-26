
# def func_90(val):
#     scoreline = 90

#     if(val>scoreline):
#         print('pass')
#     else:
#         print('failed')

# def func_60(val):
#     scoreline = 60

#     if(val>scoreline):
#         print('pass')
#     else:
#         print('failed')

# func_90(89)
# func_60(89)


def func(scoreline):
    def cmp(val):
        if(val>scoreline):
            print('pass')
        else:
            print('failed')
    return cmp

f_90 = func(90)
f_90(89)

print(type(f_90))
print(f_90.__closure__)

f_60 = func(60)
f_60(89)
