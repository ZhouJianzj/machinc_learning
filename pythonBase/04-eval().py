# 需要注意 eval()是去掉左右的引号
s = 'hello'
hello = '你好周健!'
print(eval(s))

# eval()一般配合input一起使用
age = eval(input("请输入你的年龄"))
print(type(age))


age = int(input("请输入你的年龄"))
print(type(age))
