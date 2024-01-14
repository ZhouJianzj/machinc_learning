import os
from multiprocessing import Process

from process.MyProcess import MyProcess


def thread_one(index):
    print(index, '----当前进程的pid=', os.getpid(), '当前进程的父pid=', os.getppid())


def thread_two(index):
    print(index, '----当前进程的pid=', os.getpid(), '当前进程的父pid=', os.getppid())


if __name__ == '__main__':
    print('main开启启动')
    # 当Process()中没有指定target的时候会执行Process也就是父类的run（）方法
    # p1 = Process()
    # p2 = Process()

    p1 = Process(target=thread_one)
    p2 = Process(target=thread_two)
    p1.start()
    p2.start()
    # 终止进程执行
    p1.terminate()
    p2.terminate()

    print('main执行结束')
