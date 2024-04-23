import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        # 获取新创建文件的文件名和扩展名
        file_name, file_extension = os.path.splitext(os.path.basename(event.src_path))

        # 检查文件扩展名是否为.mp4
        if file_extension.lower() == '.mp4':
            # 创建对应的.txt文件
            txt_file_name = f"{file_name}.txt"
            file_context = input("请输入内容：")

            with open("标签.txt", 'r', encoding='utf-8') as txt_file:
                file_content = txt_file.read()
            # 写入指定内容到.txt文件
            with open(txt_file_name, 'a', encoding='utf-8') as txt_file:
                txt_file.write( "第" + file_name + "集：" + file_context + file_content)

            # 显示.txt文件内容
            with open(txt_file_name, 'r', encoding='utf-8') as txt_file:
                file_content = txt_file.read()
                print(f"文件内容:\n{file_content}")


if __name__ == "__main__":
    # 指定监听的文件夹路径
    folder_path = "."  # 可以修改为你希望监听的文件夹路径

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=folder_path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

#
# def append_file(source_file, target_file):
#     try:
#         # 打开源文件并读取内容
#         with open(source_file, 'r', encoding='utf-8') as source:
#             content_to_append = source.read()
#
#         # 打开目标文件并追加内容
#         with open(target_file, 'a', encoding='utf-8') as target:
#             target.write(content_to_append)
#
#         print(f"内容已成功追加到 {target_file} 中。")
#
#     except FileNotFoundError:
#         print("文件不存在，请检查文件路径。")
#
# # 获取用户输入的文件名
# # source_filename = input("请输入要追加的文件名：")
# target_filename = input("请输入被追加的文件名：")
#
# # 调用函数进行文件内容追加
# append_file("标签.txt", target_filename + ".txt")
