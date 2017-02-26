
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for val in d.values():
    print(val)
for key,val in d.items():
    print(key,val)

print('-------------------')

for char in 'ABC':
    print(char)

print('-------------------')

from collections import Iterable
bools = isinstance('abc', Iterable) # str是否可迭代
print(bools)
bools = isinstance([1,2,3], Iterable) # list是否可迭代
print(bools)
bools = isinstance(123, Iterable) # 整数是否可迭代
print(bools)

print('-------------------')
for key,val in enumerate(['A', 'B', 'C']):
    print(key,val)

print('-------------------')
for x, y in [(1, 11), (2, 22), (3, 33)]:
    print(x, y)