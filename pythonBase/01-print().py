name = "zhoujian"
# 你的姓名是:zhoujian
print("你的姓名是:" + name)
# 你的姓名是: zhoujian
print("你的姓名是:", name)
# 你的姓名是:-zhoujian
print("你的姓名是:", name, sep="-")
# 你的姓名是:-zhoujian-->
print("你的姓名是:", name, sep="-", end="-->")
# 还可以将内容输出到指定文件
fp = open("printOutFile.txt", "w")
print("你好我是", "周健", sep="-", end="--end", file=fp, flush=True)
fp.close()

"""
print() 输出格式化
"""
# 格式化字符
name = "小米"
print("你好%s" % name)

# 格式化浮点数指定保留小数位
floatValue = 1.2
print("浮点数为%f" % floatValue)
print("浮点数为%.2f" % floatValue)

# 多个参数时
name = "xiao"
name2 = "ming"
print("我姓%s,名叫%s" % (name, name2))

#位数不够填充  %02d 0表示填充的数字 2表示几位
age = 2
print("age为%03d" % age)

# f格式：语法 print(f'你好{var}')
id = 1001
print(f'当前ID为{id}')

