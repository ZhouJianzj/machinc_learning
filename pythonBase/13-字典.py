# 字典
# 原始创建方式1
a = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(a)

# 创建dict方式2
lst1 = [1, 2, 3, 4]
lst2 = ['name', 'age', 'address']
zip_a = zip(lst1, lst2)
# <zip object at 0x0138CCB0>
print(zip_a)
# [(1, 'name'), (2, 'age'), (3, 'address')]  转换成list
# print(list(zip_a))
# 这一行的实现需要将list(zip_a)注解掉
a = dict(list(zip_a))
b = a
print(b)

# 创建字典方式3
b = dict({'name': 'zhoujian'})
c = dict(name='zhoujian', age=24)
print(c)
print(b)
# key 可以为tuple但不可以是list
key = (1, 3)
b = dict({key: 3})
print(b)

# dirt遍历
for key, value in a.items():
    print(f'key={key} value={value}')

for key in a.keys():
    print(key)

for value in a.values():
    print(value)

for item in a.items():
    print(item, type(item))
    print(item[1])

print(len(a))
# 按照key
print(min(a))
print(max(a))
print(1 in a)

# 根据指定的key获取value的两种方式
a = dict(name='zhoujian', age=25, address='test')
# 第一种
print(a.get('name'))
print(a.get('test', '不存在'))
# 第二种
print(a['name'])

# 关于字典特有的几个方法以及常用方法
print(a.popitem())
print(a.pop('test', '不存在这个key'))

print(list(a.values()))
print(tuple(a.values()))

print(a.items())
print(list(a.items()))
print(tuple(a.items()))

# 字典的生成式表达式
lst1 = ['age', 'name']
lst2 = ['27', 'zhoujian']
# {key:value for item in range(....)}
a = {lst1[i]: lst2[i] for i in range(len(lst2))}
print(a)
print(type(zip(lst1,lst2)))
# {key:value for key,value in zip(list1,list2)}
a = {key: value for key,value in zip(lst1,lst2)}
print(a)


