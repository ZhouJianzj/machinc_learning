# 随机生成1-100之间的随机数,使用列表装然后找出其最大值,不许使用max函数
import random


def get_max(lst):
    max = lst[0]
    for i in range(1,len(lst)):
        if max < lst[i]:
            max = lst[i]
    return max
lst = [random.randint(1,100) for item in range(10)]

print(get_max(lst),lst)