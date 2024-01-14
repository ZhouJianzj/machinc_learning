# 元组
# 元组当只有一个元素的时候 , 是不能省略的
import random

b = ('hello',)
print(b)

a = tuple('hello')
print(a)

a = tuple(item for item in range(10))
print(a)

a = tuple(random.randint(1, 10) for item in range(2))
print(a)

a = tuple(item for item in range(1, 11) if item % 2 != 0)
print(a)

# 元组的遍历

for item in a:
    print(item, end=' ')

print()

for index in range(0, len(a)):
    print(a[index], end=' ')

print()

for index, item in enumerate(a):
    print(f'index={index}  item={item}', end=' ')

print()
print(f'count()=====> {a.count(1)}')

print(f'index()=====> {a.index(3)}')


# tuple也支持切片操作的
b = a[0:1:1]
print(type(b))
print(id(b))
print(id(a))
print(b)
del (a)
print(a)
