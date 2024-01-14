# 列表list
import random

lst1 = list("hello")
print(lst1)
lst2 = list(range(1, 20, 2))
print(lst2)

lst3 = [1, 1, 'zhoujian', 'helloworld']
print(lst3)

print(f"l出现的次数为{lst1.count('l')}")
print(max(lst2))
print(min(lst2))
print(lst2.index(3))
print(len(lst2))
print(2 in lst2)
print(2 not in lst2)

# 列表的遍历几种方式********************************************
# 第一种
list = ["hello", "world", "java", "python"]
for item in list:
    print(item, end=" ")

print()
# 第二种
for item in range(0, len(list)):
    print(list[item], end=" ")

print()
# 第三种
for index, item in enumerate(list):
    print(index, item, end=" ")
    print(list[index])

# 列表的常用方法
print(list)
list.append("你好")
list.append("你好")
print(list)

# 元素在list中第一次出现的下标
print(list.index("你好"))
# 统计出现的次数
print(list.count("java"))
print("原始list内存地址", id(list))
# 复制出一个新得到数组
list1 = list.copy()
print(f"copy之后的list1内存地址{id(list1)}原始list内存地址{id(list)}")
print(list)
# 指定下标弹出，先打印被弹出的元素然后弹出
print(list.pop(1))
print(list)
# 指定某个元素移除
list.remove("你好")
print(list)

# 列表生成式语法 lst =  expression for item in ranger(...)
lst = [item for item in range(1, 11)]
print(lst)
lst = [item * item for item in [2, 3, 4]]
print(lst)
# for循环出来的元素可以不使用
lst = [random.randint(0, 1) for item in range(10)]
print(lst)
lst = []

# 创建二位数组
lst = [
    [1, 2, 3, 4],
    [1, 3, 4, 5],
    ['zhoujian', 'nihao']
]
print(lst)
# 遍历二维数组
for a in lst:
    for b in a:
        print(b, end=' ')
    print()

# 列表生成式生成二维数组
lst = [[b for b in range(1, 6)] for a in range(1, 6)]
print(lst)
# 遍历二维数组
for index_a, a in enumerate(lst):
    for index_b, b in enumerate(a):
        print(index_b, "----", b, end=' ')
    print(index_a)

# 列表的删除
del(lst)
# 列表删除了就发访问不了会报一个错误  
print(lst)