# 单分支
a = 10
# 第一种写法
if a > 10:
    print("a 大于 10 ")
else:
    print("a 小于 10 ")

# 第二种写法
print("a 大于 10 " if a > 10 else "a 小于 10 ")

# 单个if 并且后面只有一个语句的时候可以这样写
if a > 8: print("true")

# 类似 if ... else if 写法
inputValue = eval(input("请输入数字"))
if inputValue == 10:
    print("a 等于 10 ")
elif inputValue == 20:
    print("a 等于 20 ")

input_value = eval(input("请输入数字"))
if input_value == 10:
    input_value1 = eval(input("请输入数字"))
    if input_value1 == 1010:
        print("你输入的数字分别位10 ------1010")
    else:
        print(f"你输入的数字为10 ------ {input_value1}")
else:
    print("你输入的数字不是10")

# 模拟用户登入输入账号和密码都需要正确案例
username = input("请输入用户名：")
password = input("请输入密码：")
if username == 'zhoujian' and password == '123123':
    print('登录成功！')
else:
    print('你输入的账户和密码不匹配！')
