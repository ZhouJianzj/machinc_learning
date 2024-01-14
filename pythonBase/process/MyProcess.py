import multiprocessing


# 创建进程的第二种方式 继承的方式
class MyProcess(multiprocessing.Process):
    def __init__(self, name):
        super(MyProcess, self).__init__()
        self.name = name

    def run(self):
        print(f"你好我是{self.name}")
