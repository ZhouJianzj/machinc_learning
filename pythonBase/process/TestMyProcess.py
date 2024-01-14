from process.MyProcess import MyProcess

if __name__ == '__main__':
    print('main开始执行')
    for index in range(8):
        p1 = MyProcess(f'name{index}')
        p1.start()
        p1.join()
    print('main执行结束！')

