import threading
from threading import Thread
from time import sleep


def do_things():
    for index in range(20):
        print(threading.currentThread().name, '------', index)


# 方式二
class MyThread(Thread):
    def run(self) -> None:
        print(self.name)


num = 100


# 加法
def add():
    global num
    num += 10
    print(threading.current_thread().name, '----', num)


#  减法
def sub():
    global num
    num -= 10
    print(threading.current_thread().name, '----', num)


if __name__ == '__main__':
    # Thread方式一
    # theads = [Thread(target=do_things, name=f"thread{index}") for index in range(10)]
    # for thread in theads:
    #     thread.start()
    #
    # for thread in theads:
    #     thread.join()

    # 方式二
    # threads = [MyThread() for index in range(10)]
    # for thread in threads:
    #     thread.start()

    #     多个线程之间数据共享吗
    print(num)
    for index in range(1):
        p1 = Thread(target=add)
        p1.start()
    for index in range(1):
        p2 = Thread(target=sub)
        p2.start()
    print(num)