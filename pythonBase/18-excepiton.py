'''
异常处理
'''

# 基础语法
try:
    a = 10 / 0
except:
    print("分母为0了！")

# 可以捕获多个异常建议先子类后父类
try:
    pass
except ValueError:
    pass
except BaseException:
    pass
except Exception:
    pass

# else只有在没有发生异常的是时候才会执行
try:
    a = 10 / 1
except:
    print("分母为0了！")
else:
    print("异常没有发生")

# finally 无论异常发生还是没有发生都会执行

try:
    a = 10 / 0
except Exception as e:
    print(e, "异常发生了============分母为0了")
else:
    print("异常没有发生")
finally:
    print("无论异常发没发生都会执行")

"""
抛出异常
"""
input = "zj"
try:
    if input != "1" or input != "0":
        # raise 关键字
        raise Exception("你输入的不是   1  或者   0 ")
    else:
        print(f'你输入的是{input}')
except Exception as e:
    print(e)
