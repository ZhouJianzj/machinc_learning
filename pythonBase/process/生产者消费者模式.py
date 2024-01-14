# 生产者线程
from multiprocessing import Queue
from threading import Thread


def producer(q):
    for index in range(5):
        q.put(index)
        print(f'消费者存入了-------{index}')


# 消费者线程
def consumer(q):
    for index in range(5):
        msg = q.get()
        print(f"生产者消费了-------{msg}")


if __name__ == '__main__':
    queue = Queue()

    t1 = Thread(target=producer,args=(queue,))
    t2 = Thread(target=consumer,args=(queue,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()