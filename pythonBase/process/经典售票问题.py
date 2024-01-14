import threading
from threading import Thread, Lock
from time import sleep

ticket = 50
lock = Lock()


def sale():
    global ticket
    # 每个窗口有100个人排队
    for i in range(100):
        # 拿锁
        lock.acquire()
        if ticket > 0:
            ticket -= 1
            print(f'{threading.currentThread().name}当前剩余：{ticket}')
            sleep(0.5)
        # 释放锁
        lock.release()


# 10个线程模拟10个售票窗口
for i in range(10):
    thread = Thread(target=sale)
    thread.start()
