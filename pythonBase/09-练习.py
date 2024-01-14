# 判断是闰年还是平年 闰年能被4整除但是不能被100整除，或者被400 整除
year = eval(input("please input your year"))
print(f"{year}为闰年") if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else print(f'{year} 是平年')

# 打印乘法口诀表
for a in range(1, 10):
    for b in range(1, a + 1):
        print(a, "*", b, '=', a * b, end="\t")
    print()

# 猜数字游戏随机生成1 ~ 50 之间的数字
import random

randomNumber = random.randint(1, 50)
num = 0
while True:
    inputValue = eval(input("please input your answer number!"))
    if randomNumber == inputValue:
        if num == 1:
            print(f"你好棒!第一次就猜中了随机数为{randomNumber}")
            break
        elif num == 3:
            print(f"第3次你猜对了随机数为{randomNumber}")
            break
        else:
            print(f"第{num}次你猜对了随机数为{randomNumber}")
            break
    else:
        if inputValue > randomNumber:
            print("输入的数字  大了")
        else:
            print("输入的数字   小了")
    num += 1
