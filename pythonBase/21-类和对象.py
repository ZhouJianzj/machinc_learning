# 类的定义包括 类属性  实例属性 实例方法发 静态方法 类方法
# () 可以省略不写,()是用来继承别的使用的
class Student():
    # 类属性
    school = "niit"

    # 实例属性  类似于java中的构造方法 ,self 类似this
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法
    def method_entity(self):
        # 可以调用任何属性
        self.name
        self.age
        self.school
        Student.school

    # 叫静态方法
    @staticmethod
    def method_static():
        # 只可以调用类属性
        Student.school

    # 类方法
    @classmethod
    def method_class(cls):
        # 只可以调用类属性
        cls.school


# 创建对象
xiaoming = Student("xiaoming", 19)
xiaoming.method_entity()
xiaoming.method_static()

#属性和方法动态绑定
# 属性(实例属性、类属性)
zhangsan = Student("zhangsan",20)
zhangsan.sex = "男"
print(zhangsan.sex)
# print(xiaoming.sex)

Student.address = "南京"
print(zhangsan.address)
print(xiaoming.address)

# 方法(实例方法)
def method1():
    print("我是动态绑定的方法")
zhangsan.fun_dynamic = method1
zhangsan.fun_dynamic()
# xiaoming.fun1()

def method2():
    print("我是动态绑定的静态方法")
Student.fun_dynamic_static = method2
Student.fun_dynamic_static()
# TypeError: method2() takes 0 positional arguments but 1 was given
# zhangsan.fun_dynamic_static()