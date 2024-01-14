# 线程池的概念
import os
import time
from multiprocessing import Pool


def task(name):
    print(f"当前进程{name},当前进程pid为{os.getpid()},父进程的pid为{os.getppid()}")


if __name__ == '__main__':
    print('main进程启动')
    start_time = time.time()
    p = Pool(2)
    for index in range(1000):
        # 异步执行
        # p.apply_async(func=task, args=(index,))
        # 同步阻塞执行
        p.apply(func=task, args=(index,))
    # 表示进程池不在接收新的任务了，准备开始执行了
    p.close()
    p.join()
    # 不管任务有没有执行完毕都会终止!
    p.terminate()
    print('main进程结束',time.time()-start_time)