# set 是无序不可重复的
# 创建set
a = {'name', (1, 3, 4), 'name'}
print(a)

# TypeError: unhashable type: 'list set中的元素不允许是list
# a = {[1,2,3,4],[1,3,6],'test'}

'''
 使用set() 创建集合
'''
a = set()
print(bool(a))
print(a, type(a))
# 这个创建的是一个dict类型
a = {}
print(a, type(a))
a = set('hello')
print(a)
a = set((1, 2, 3, 4))
print(a)
a = set({1, 2, 3, 4})
print(a)
a = set(range(10))
print(a)
a = set(item for item in [1, 2, 3, 5])
print('from for', a)

print(max(a))
print(min(a))
print(len(a))
print(1 in a)
print(bool(a))

print(a)
a.add("zhoujian")
print(a)
a.pop()
print(a)
b = {1, 2}
a = {1, 3}
# a.update( b)
# print(a)
# 交集
print(a & b)
# 并集
print(a | b)
# 差集
print(a - b)
# 补集
print(a ^ b)

print(a)
# a.remove(3)
print(a)
print(a.difference(b))

# 集合的遍历
for item in a:
    print('遍历集合元素', item)
# for index in range(len(a)):
#     print(a.)
for index, item in enumerate(a):
    print(index, item)
