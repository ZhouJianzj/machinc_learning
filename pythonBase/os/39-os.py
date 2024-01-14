# 资源目录的操作
import datetime
import os

# 获取当前的工作目录
pwd = os.getcwd()
print(pwd)

# 创建单个文件夹
# os.mkdir("aa")
# 创建多层文件夹
# os.makedirs("bb/cc")
# 删除空的文件夹
# os.rmdir('aa')
# 删除多层目录
# os.removedirs("bb/cc")
# 切换当前工作目录
# os.chdir("aa")
# print(os.getcwd())

# 遍历目录树
# os.chdir("E:\workspace\pythonSpace\pythonBase")
# for dirs in os.walk(os.getcwd()):
#     print(dirs)
# print(files)

# 删除文件
# os.remove("E:\workspace\pythonSpace\pythonBase\os\\aa\zj.txt")
# 重命名
# os.rename('zhoujian .txt','zhoujian.txt')


# 获取文件信息的
# os.stat_result(st_mode=33206, st_ino=3940649674530974, st_dev=4143944105,
# st_nlink=1, st_uid=0, st_gid=0, st_size=26, st_atime=1704265791, st_mtime=1704247417, st_ctime=1704265769)
# st_atime:最近一次访问时间
# st_ctime:创建时间
# st_mtime:最后一次修改时间

import time

# 获取文件时间信息并且格式化
def time_format(t):
    format_time = time.strftime("%Y-%m-%d :%H-%M-%S", time.localtime(t))
    return format_time


info = os.stat("zhoujian.txt")
print(info)
print(info.st_ctime)
print(time_format(info.st_ctime))
