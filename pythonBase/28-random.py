import random

print('生成[0.0，1.0）之间的随机数', random.random())
print('生成[1,3]之间的随机数', random.randint(1, 3))
# 指定范围[1,5)，并指定步长
print(random.randrange(1, 5, 2))

# 生成指定区间的小数[a,b]
print(random.uniform(1.1, 1.3))

# 在序列中随机选择一个元素
lst = [item for item in range(10)]
print(random.choice(lst))

# 将序列中的元素随机排列，返回打乱之后的序列
random.shuffle(lst)
print(lst)
