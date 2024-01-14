"""
_:表示受保护的
__:表示私有的
"""


class Student:
    aa = "test"
    _school = '周健'
    __address = '南京'

    def __init__(self, age, gender):
        self._age = age
        self.__gender = gender
        self.aa = age

    # getter
    @property
    def getGender(self):
        return self.__gender

    # setter
    @getGender.setter
    def setGender(self, gender):
        self.__gender = gender
    # del
    @getGender.deleter
    def delGender(self):
        del self.__gender

    def _method_protected(self):
        print(self.aa)
        pass

    def __method_private(self):
        print(self.aa)
        pass

    @staticmethod
    def __method_static_private():
        print(Student.aa)
        pass

    @staticmethod
    def _method_static_protected():
        pass

    @classmethod
    def __method_class_private(cls):
        print(cls.aa)
        pass

    @classmethod
    def _method_class_protected(cls):
        pass


zhoujian = Student(28, "男")
print(zhoujian._school)
# 展示所有私有属性和方法
print(dir(zhoujian))
# 不推荐这么使用,推荐setter and getter方式去使用
print(zhoujian._Student__address)
print(zhoujian.aa)

# setter and getter private属性
# getter
print(zhoujian.getGender)
zhoujian.setGender = 'nan'
print(zhoujian.getGender)
