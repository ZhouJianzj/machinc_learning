# 多态,不关心变量类型以及是否有继承关系

class Person:
    def eat(self):
        print("人爱吃蔬菜!")


class Cat:
    def eat(self):
        print("小猫爱吃鱼!")


class Dog:
    def eat(self):
        print("小狗爱吃骨头!")


def fun(obj):
    obj.eat()


# 是不是就形成了多太
c = Person()
cc = Cat()
ccc = Dog()
fun(c)
fun(cc)
fun(ccc)

print(10/3)
