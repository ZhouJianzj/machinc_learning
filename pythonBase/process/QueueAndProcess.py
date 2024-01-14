# 队列和进程
from multiprocessing import Queue, Process

num = 100


# 往queue中添加元素
def add(queue):
    global num
    if not queue.full():
        for index in range(10):
            num -= 10
            queue.put(num)


# 获取queue种每一个元素
def read_result(queue):
    if not queue.empty():
        for item in range(queue.qsize()):
            print(queue.get())


"""
在你的代码中，每个进程都有自己的内存空间，因此它们之间并不共享全局变量 num。虽然你在 add 函数中对 num 进行了修改，
但这个修改只影响到了当前进程的内存空间，不会影响其他进程。如果你希望多个进程之间共享数据，可以使用 multiprocessing 
模块中的 Value 或 Array，或者使用 multiprocessing.Manager 中的 Value 或 Array。这些对象可以在多个进程之间共享，
从而实现进程间通信。
"""
if __name__ == '__main__':
    # 没有指定数字表示可以接收无数个
    q = Queue()
    p1 = Process(target=add, args=(q,))
    p3 = Process(target=add, args=(q,))

    p2 = Process(target=read_result, args=(q,))
    p1.start()
    p1.join()
    p3.start()
    p3.join()
    p2.start()
    p2.join()
