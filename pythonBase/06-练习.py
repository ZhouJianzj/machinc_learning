inputValue = eval(input("请输入一个四位数的数字："))
# 输出个位数
a = inputValue % 10
print(f'个分为数位:{a}')
# 输出十位数
b = inputValue // 10 % 10
print(f'十分为数位:{b}')
# 输出百位数
c = inputValue // 10 // 10 % 10
print(f'百分为数位:{c}')
# 输出千位数
b = inputValue // 10 // 10 // 10 % 10
print(f'千分为数位:{b}')
print(inputValue)