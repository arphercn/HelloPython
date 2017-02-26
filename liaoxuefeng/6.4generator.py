#第一种生成方式 []变成()
# L = [x * x for x in range(10)]
# print(L)
g = (x * x for x in range(10))
print(g)
for n in g:
    print(n)
print('--------------------')


#第二种生成方式 yield()
# 著名的斐波拉契数列（Fibonacci）
# def fib(max):
#     n, a, b, tmp = 0, 0, 1, 0
#     while n < max:
#         tmp = a
#         a = b
#         b = tmp + b
#         # a, b = b, a + b
#         print(b)
#         n = n + 1
#     return 'done'

# fib(5)

def fibo(max):
    n, a, b = 0, 0, 1
    while n < max:
        a, b = b, a + b
        yield b
        n = n + 1
    return 'done'

for i in fibo(5):
    print(i)