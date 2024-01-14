"""
计算圆的周长和面积
"""


class Circle:
    def __init__(self, r):
        self.r = r

    # 计算圆的面积
    def getArea(self):
        return self.r ** 2 * 3.14

    # 计算圆的周长
    def getPerm(self):
        return self.r * 3.14 * 2


# 创建对象
r = eval(input("请输入圆的半径r:"))
c = Circle(r)

# 调用方法
area = c.getArea()
perm = c.getPerm()
print(f'圆的面积为：{area}  圆的周长为：{perm}')

"""
定义学生类录入 5个学生对象存储到列表中
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + ":" + str(self.age)


lst = []
for i in range(1, 6):
    s = Student('zhoujian' + str(i), 18 + i)
    lst.append(s)

for item in lst:
    print(item)
