s = 'hello world'
for i in range(len(s)):
    print(s[i])

# 切片操作
str = 'hello_world'
# start:闭区间  end:开区间  step:默认为1  start + step
print(str[0:len(str):1])
print(str[::1])
print(str[0::])
print(str[::])

# 切取指定范围的 h
print(str[0:1:1])

# 倒叙
# -len() -1
print(str[-1:-len(str) - 1:-1])
print(str[-1::-1])
print(str[:-len(str) - 1:-1])
print(str[::-1])

print(str[-len(str): -len(str) + 6: 1])

print('he' in str)
print('lx' not in str)
print(max(str))
print(min(str))
print(str.index('e'))
print(str.count('l'))

for i in range(len(str)):
    print(str[i], ord(str[i]),sep="--")
