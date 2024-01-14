"""变量"""
name = "小米"
# 可以批量赋值
name1 = name2 = name
print(name2)
# 获取内存地址
print(id(name))
print(id(name1))
print(id(name2))
# 转换成字符编码
print(ord('小'))
print(chr(23567))
# 复数的表现形式
fushu = 100 + 101j
print("实数", fushu.real, "虚数", fushu.imag)
# 获取保留字段
import keyword

print(keyword.kwlist)
print(len(keyword.kwlist))

"""数据类型"""
a = 1
print(type(a))
b = 2.0
print(type(b))
# 字符串类型以及方法**************************************************************
c = "Hello"
print(type(c))
"""字符串切片  
1.正向 0 ~ N
2.反向 -N ~ -1
切片语法 s[index1:index2] 取值为左闭右开 [index1,index2)
"""
# Hell 左边不写默从0开始
print(c[:4])
# ello 右边不写默认从-1开始
print(c[-4:])
# H
print(c[0:1])
# 字符串类型进行乘法运算 s * n 表示复制多少份
print(c * 10)
# 判断c字符里里面是否包含某个字符或者字符串
print("w" in c)
print("He" in c)
print("Hllo" in c)

d = ["list1", "list2"]
print(type(d))
e = ("tuple1", "tuple2", "tuple3")
print(type(e))
f = {"set1", "set2"}
print(type(f))
g = {"key1": "name1", "key2": "value2"}
print(type(g))

"""进制"""
id = 10
id1 = 0b1011
# 八进制 15
id2 = 0o17
# 十六进制23
id3 = 0x17
print(f'id1 = {id1} id2 = {id2} id3 = {id3}')
# 数据类型转换
i = int("10")
i = float(1.0)
i = str(19)
# 将十进制转换成十六进制
i = hex(15)
# 将十进制转换成八进制
i = oct(10)
# 将十进制转换成二进制
i = bin(8)
# 将unicode 编码转换成字符
i = chr(98)
# 将字符转换成unicode编码
i = ord("b")
print(i)


i = 10 / 3
# round()函数指定浮点数保留的浮点位个数
print(round(i, 2))
