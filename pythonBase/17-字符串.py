# 字符串常用的方法
s = '_zh_ou_jian'
print('转换成小写', s.lower())
print("转换成大写", s.upper())
print('分割字符串没有指定分割字符', s.split())
print('分割字符串指定字符', s.split('_'))
print('字符z出现的次数', s.count('z'))
print("查找指定字符串可以不指定开始和结束位置，找到返回对应索引，找到不返回-1", s.find("_", 0, len(s)))
print("第一次出现的索引，没有就报错", s.index("_"))
print('判断是否以指定字符串开头', s.startswith("z"))
print('是否以指定字符串结尾', s.endswith("j"))
print(s.replace('_', " "))

print('以行20个字符为大小，中心对其，以空格填充', s.center(20), sep="\n")
print('指定填充字符', s.center(20, "*"), sep="\n")
print(s)
print("在周健的每一个字符串后追加 s", s.join('test'))
s = 'jzzhoujianzj'
print("去掉左侧和右侧的字符串", s.strip('z'))
print(s.lstrip('j'))
print(s.rstrip('j'))
s = '_zhou_jian_'
print('从字符串末尾一直到起始', s.rsplit('_'))
print(s.split('_'))

'''字符串格式虎啊format'''
print("你叫什么{0},你今年多大了{1}".format("zhoujian", 18))

a = 123000
print('占位符-分隔符（：）- 左对齐（<）-行宽', '{0:*<20}'.format(a))
print('{0:->20}'.format(a))
print('{0:-^20}'.format(a))
print('{0:,}'.format(a))
a = 3.141234235
print('{0:.2f}'.format(a))
print('{0:.2%}'.format(a))

s = "周健"
# 默认utf-8  error可选为strict 'ignore', 'replace'
s_encode = s.encode()
print(s.encode(errors='strict'))
print(s_encode.decode(errors='replace'))

s_utf_encode = s.encode('utf', errors='replace')
print(s_utf_encode)

s_gbk_encode = s.encode('gbk')
print(s_gbk_encode)

print("*" * 50)
# 判断是不是十禁止的阿拉伯数字
lsts = ["一", "壹", "0b10101", "0o102", "0x10A", "IV", "123"]
for item in lsts:
    print(item, ".isdigit()=", item.isdigit())

print("*" * 50)
# 所有字符都是数字或字母 (包含中文字符)
for item in lsts:
    print(item, ".isalnum=", item.isalnum())

print("*" * 50)
# 所有字符都是数字
for item in lsts:
    print(item, ".isnumeric()=", item.isnumeric())

# 所有字符都是字母(包含中文字符）
print("*" * 50)
for item in lsts:
    print(item, "isalpha()=", item.isalpha())

s = "sS"
print(s.islower())
s = "SS"
print(s.isupper())
s = "Zhou Jian"
# 判断所有字符都是首字母大写
print(s.istitle())

print("{0:*^50}".format("isspace()"))
s = " "
print(s.isspace())
s = "\t"
print(s.isspace())
s = "\n"
print(s.isspace())
s = ""
print(type(s))
# false
print(s.isspace())
print(len(s))

print("{0:*^50}".format("字符串拼接"))
s = "-"
# s 是连接符 join里面的是需要被链接的对象
print(s.join("test"))
print("".join(["name", "age", "address"]))

# 字符串去重操作

s = "hehhhllllo"
ss = ""
for item in s:
    if item not in ss:
        ss += item
print(ss)

ss = ""
for index in range(len(s)):
    if s[index] not in ss:
        ss += s[index]
print(ss)

# 通过集合去重
set_s = set(s)
lst_s = list(set_s)
lst_s.sort(key=s.index)
print("".join(lst_s))


s = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
set_s = set(s)
lst_s = list(set_s)
# Sort lst_s based on the order of elements in the original list s
lst_s.sort(key=lambda x: s.index(x))

