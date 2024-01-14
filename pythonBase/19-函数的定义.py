# 函数的定义
# 正常函数的定义和调用
def test(arg):
    print("test method executing arg = ", arg)


test("zhoujian")


# 多个参数的函数以及参数传递
def method(name, age):
    print(f'name = {name}  age = {name}')


method("zhoujian", 18)
# method(name="zhoujian",18) 这样是不可以的
method("zhoujian", age=18)
method(age=18, name='zhoujian')


# method() 参数没有默认值需要传参


def method1(name="zhoujian", age=19):
    print(f'name = {name}  age = {name}')


method1()  # 入参有默认值可以不传
method1('zhoujian', 18)
method1(age=18)
method1(name='zhoujian')
# method1('zj',name='zhoujian')  这样也是不可以的，在方法定义的时候赋默认值的参数最好放在最后面
method1("zhoujian", age=18)

'''
 函数接收多个入参
'''


# 这种不是键值对的参数声明最后会传入的参数使用有一个元组去接 ，声明方式  *
def method2(*params):
    print(type(params))
    for item in params:
        print(item, end=' ')


method2(1, 2, 3, 4, "zhoujian")
print()
# 如何参数是一个元组或者是一个列表或者是一个集合，使用 * 可以拆解
method2(*(1, 2, 3))
print()
method2(*[1, 2, 3, 4])
print()
method2(*{1, 2, 3, 4, 5})


# 参数声明为键值对的入参并允许接收多个使用 **

def method3(**kvparams):
    print(type(kvparams))
    for key, value in kvparams.items():
        print(key, '=', value)


method3(name='zhoujian', age=18)
method3(**{'name': 'zhoujian', 'age': 18})
method3(**dict(name='zhoujian', age=18))
lst1 = ['name', 'age']
lst2 = ['zhoujian', 20]
# print(zip(lst1,lst2))
print(list(zip(lst1, lst2)))
method3(**dict(zip(lst1, lst2)))

'''
 函数的返回值
'''


def method4(num):
    sum = 0
    oddSum = 0
    evensum = 0
    for item in range(1, num + 1):
        sum += item
        if item % 2 != 0:
            evensum += item
        else:
            oddSum += item
    return sum, oddSum, evensum


# 多个返回值的时候会被封装成一个元组
print(method4(10))
# 也可以将其拆解
a, b, c = method4(10)
print(a, b, c)

'''
变量的作用域
'''
s = 100


# s 为全局变量可以在局部作用域中被使用
def test(a, b):
    ss = s + a + b
    print(ss)


test(1, 2)


# 当局部变量和全局变量重名的时候 局部作用域中局部变量优先
def test1():
    s = 1
    print(s)


test1()


# 在局部作用域中声明全局变量
def test2():
    global a
    a = 100
    return a


print(test2())

'''
匿名函数 lamba
'''
s = lambda x: x + 1
ss = s(1)
print(ss)

# 在列表遍历时 使用lambda函数
lst = [1, 2, 3, 4]
for i in range(len(lst)):
    item = lambda a: a[i]
    print(item(lst))

# 字典排序的时候
dict = [
    {'name': 'zhoujian', 'age': 19},
    {'name': 'xiaozhang', 'age': 20},
    {'name': 'xiaohong', 'age': 11},
    {'name': 'baga', 'age': 10},
]
# 方向排序倒叙
dict.sort(key=lambda x: x.get('age'), reverse=True)
print(dict)


# 这样定义，方法在调用的时候会有入参提示
def aa(key: int = ...):
    print(key)


aa()

# 函数的递归调用，不建议使用内存占用比较大


# 常用的数学函数
# 取绝对值
print(abs(0), abs(10), abs(-10))
# 取商和余数
print(divmod(10, 3), type(divmod(10, 3)))
# 取最大值和最小值
print(max(range(1, 10)))
print(min(range(1, 20)))
# 求和
print(sum(range(10)))
# 求一个数的多少次幂
print(pow(2, 2))

# 保留小数，默认不保留并且四舍五入
print(round(3.212))
print(round(2.35, 1))
# 复数保留个位数依次类推，
print(round(2.345, -1))
print(round(round(254.44), -2))

"""
迭代器函数
"""
lst = [1, 3, 456, 7, 899]
print(sorted(lst))
print(sorted(lst, reverse=True))

print(reversed(lst), list(reversed(lst)))
zip_var = zip(range(1, 4), range(1, 5))
# print(list(zip_var))
print(tuple(zip_var))

# 可以指定起始index
print(enumerate(lst), list(enumerate(lst, start=1)))
print(enumerate(lst), list(enumerate(lst)))

# 判断迭代器对象中所有的元素都是true,0的bool()为False
print(all([1, 2, 3, 0]))
# 如果bool（x）对于可迭代对象中的任何x都为True，则返回True
print(any([0, 0, 0, 1, 0]))

# 过滤器
print(list(filter(lambda x: x % 2 != 0, range(10))))


def fun(x):
    return x % 2 != 0


# 写函数名字不需要带()
print(list(filter(fun, range(10))))

# map操作
print(list(map(lambda x: x + 1, range(10))))

dict1 = {'name': 'zhoujian'}
def fun1(x):
    print(x)
    return dict1.get(x)
print(list(map(fun1, dict1)))
