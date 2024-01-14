import os
from multiprocessing import Process


def thread(index):
    print(index,'----当前进程的pid=',os.getpid(),'当前进程的父pid=',os.getppid())


if __name__ == '__main__':
    print("主线程启动！")
    threads = []
    for item in range(5):
        p = Process(target=thread,args=(item,))
        p.start()
        threads.append(p)
    # join()方法使得当前进程优先执行主线程知道当前进程执行完毕之后才执行！
    for item in threads:
        item.join()
    print("主线程结束!")