from multiprocessing import Queue

if __name__ == '__main__':
    queue = Queue(3)
    print('队列的大小', queue.qsize())
    print('队列是否为空', queue.empty())
    queue.put("one")
    queue.put("two")
    queue.put("three")
    print('队列的大小', queue.qsize())
    print('队列是否为空', queue.empty())

    #     当queue满的时候再次put的时候会出现等待状况，block默认值为True 可以是设置timeout
    #     queue.put("four")
    # put_nowait满的时候不等待直接报错，等同于put（block=False）
    # queue.put_nowait("five")
    print('出队列', queue.get())
    print(queue.get())
    print(queue.get())
    # 当queue种没有任务的时候再次get会出现阻塞样式的等待
    print(queue.get())
    # 没有时会直接抛出异常，等同于 get(block = False)
    queue.get_nowait()