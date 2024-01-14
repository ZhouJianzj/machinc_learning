import os
from multiprocessing import Process


def thread_one(index):
    print(index, '----当前进程的pid=', os.getpid(), '当前进程的父pid=', os.getppid())


def thread_two(index):
    print(index, '----当前进程的pid=', os.getpid(), '当前进程的父pid=', os.getppid())


if __name__ == '__main__':
    for index in range(5):
        p1 = Process(target=thread_one, kwargs={"index": index})
        p2 = Process(target=thread_two, args=(index,))

        p1.start()
        p2.start()
        # 判断进程是否存活！
        print(p1.name, p1.pid, p1.is_alive())
        print(p2.name, p2.pid, p2.is_alive())
        # 当前线程先执行
        p1.join()
        p2.join()
        print(p1.name, p1.is_alive())
        print(p2.name, p2.is_alive())
