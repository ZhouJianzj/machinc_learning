# 继承
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'大家好我叫{self.name},今年{self.age}')


class Student(Person):
    def __init__(self, name, age, gender):
        # super
        super(Student, self).__init__(name, age)

        self.gender = gender


class Doctor(Person):
    def __init__(self, name, age, department):
        super(Doctor, self).__init__(name, age)
        self.department = department


zhoujian = Student('zhoujian', 18, '男')
zhoujian.show()
print('*' * 88)
yanjiuqi = Doctor("mrs yan", 19, '护士')
yanjiuqi.show()

"""
 一个子类继承多父类
"""


class Person1:

    def __init__(self, msg):
        print(f'Person1 中 __init__()方法执行! msg = {msg}')


class Person2:

    def __init__(self, msg):
        print(f"Person2 中 __init__()方法执行! msg = {msg}")


print('*' * 88)


class ZJ(Person1, Person2):
    def __init__(self, msg1, msg2, name):
        # 当继承多个父类的时候使用父类className.的方式
        Person1.__init__(self, msg1)
        Person2.__init__(self, msg2)
        self.name = name
        print(f"ZJ 中 __init__()方法执行! msg = {self.name}")


zhoujian = ZJ("niit", "test", 'zhoujian')

"""
方法重写
"""


class Person3:
    def __init__(self, phone):
        self.phone = phone

    def show(self):
        print(f'Person3 中 show() msg = {self.phone}')


class Person4:
    def __init__(self, address):
        self.address = address

    def show(self):
        print(f'Person4 中 show() msg = {self.address}')


print('*' * 88)


class SuperMan(Person3, Person4):
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
    '''注意多个父类时并且多个父类被重写的方法名称相同时'''
    def show(self):
        Person3.show(self)
        Person4.show(self)
        print(self.address, self.phone, self.name)


zj = SuperMan("zhoujian", "nanjing", 123324324)
zj.show()

print('*' * 88)


class Test(Person3):

    def show(self):
        # 二选一
        super(Test, self).show()
        Person3.show(self)

        print(self.phone)

# 注意在子类没有__init__方法时候他继承父类的__init__()
test = Test(12312)
test.show()
