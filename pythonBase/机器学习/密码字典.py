import itertools as its
import threading

# 全局互斥锁
lock = threading.Lock()


def generate_passwords(start, end, filename):
    # words = "1234567890abcdefghijklmnopqrstuvwxyz!@#$%&*?."
    words = "1234567890"
    # 生成密码本的位数，repeat=8 自定义密码位数
    password_range = range(start, end)
    r = its.product(words, repeat=8)

    with lock:
        with open(filename, "a") as dic:
            for i in r:
                dic.write("".join(i))
                dic.write("\n")


# 设置线程数和密码范围
thread_count = 60  # 可根据实际情况调整
password_per_thread = 1000000  # 每个线程生成的密码数量


def main():
    filename = "./password.txt"

    # 创建并启动线程
    threads = []
    for thread_id in range(thread_count):
        start = thread_id * password_per_thread
        end = start + password_per_thread

        thread = threading.Thread(target=generate_passwords, args=(start, end, filename))
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
    print("密码本已生成")
