# 会涉及到一个内置函数range() for 的具体语法为 for value in  range: ....
for i in 'hello':
    print(i)

# range 函数的取值范围为左边右开  [index,index1) 1~10
for i in range(1, 11):
    print(i)

# 2 4 6 8 10
sum_o = 0
sum_j = 0
for i in range(1, 11):
    if (i % 2) == 0:
        sum_o += i
        print(f'1 ~ 10 之内的偶数和为{sum_o}')
    else:
        sum_j += i
        print(f'1 ~ 10 之内的奇数和为{sum_j}')

# for 和 else 的使用
for i in range(1, 11):
    print(f"你好------{i}")
else:
    print("循环结束")

# while 循环 *****************************************************************************
i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print("while 循环执行完毕！")
# 案例：实现用户只有三次输入错误用户和密码次数
# i = 1
# while i <= 3:
#     username = input("请输入用户名：")
#     password = input("请输入密码：")
#     if username == "zhoujian" and password == "123123":
#         print("系统正在加载中.......")
#         i = 10
#     else:
#         print(f"你输入的密码或账户错误你还有{3 - i}次机会")
#         i += 1
#     if i == 4:
#         print("3次机会使用完毕")


# break 跳转语句
# 不输入是0 到 9
for a in range(10):
    print(a)
    if a == 2:
        # else是不执行的
        break
else:
    print('for执行结束')

i = 0
while i <= 2:
    print(i)
    if i == 1:
        break
    i += 1
else:
    print(f'i为{i}')

#   改版后的用户登录次数限制

sum = 0
while sum < 3:
    username = input("请输入用户名称！")
    password = input("please input your password !")
    if username == "zj" and password == '123123':
        print('验证通过》》》》》》》')
        # 整合while和else都不执行了
        break
    else:
        sum += 1
        if 3 - sum != 0: print(f'还有次机会{3 - sum}')
else:
    print('你的三次以及使用完毕！')

# continue 的用办法
# 求偶数的和
sum = 0
for i in range(1, 5):
    if i % 2 != 0:
        # 下面的语句都不执行
        continue
    sum += i
    i += 1
else:
    print(f'sum = {sum}')



# pass 占位符的意思
if i in range(10):
    # 确定需要写业务逻辑但是现在还没有想好
    pass
while True:
    pass


for i in 'python':
    for j in range(2):
        print(i,end='')
        if i == 'h':
            break