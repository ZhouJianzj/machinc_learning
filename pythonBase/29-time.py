# time 模块的一些方法
import time

print(time.time())
# time.struct_time(tm_year=2023, tm_mon=12, tm_mday=31, tm_hour=14, tm_min=29, tm_sec=39, tm_wday=6, tm_yday=365, tm_isdst=0)
print(time.localtime())
time.struct_time
print(time.strftime("%Y-%m-%d", time.localtime()))
print(time.ctime())
# time.strftime("%Y-%m-%d"))
print(time.strptime("2001", "%Y"))
print("#" * 150)
"""
datetime类  比较放方便 可以直接比较大小
"""
from datetime import datetime

now = datetime.now()
print(now)
date = datetime(2010, 2, 3, 4, 5)
print(date)
print(f'年：{date.year}  月：{date.month} 日：{date.day}  时：{date.hour}  分：{date.minute}  秒：{date.second}')
# 比较两个时间的大小
print(now > date)

# datetime 类型也可和str进行转化
print(now.strftime("%Y-%m"))
str_date = "2023年12月31日"
print(datetime.strptime(str_date, "%Y年%m月%d日"))

print(now - date)

"""
timedelta 时间间隔类 加减运算
"""
from datetime import timedelta

timedelta_my =  timedelta(9)
print(datetime.now() + timedelta_my)