# 匹配
# input_value = eval(input("你请输入数据类型样式"))

s = {'a': "zhoujian"}
ss = s.copy()
s['a'] = "hello"
print(s,id(s))
print(ss,id(ss))
