"""
类的浅拷贝和深拷贝
"""


class CPU:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


cpu = CPU()
disk = Disk()
computer = Computer(cpu, disk)
# 变量(类)的赋值
computer1 = computer
print(f'computer1的内存地址{computer1}  {computer1.cpu} {computer1.disk}')
print(f'computer的内存地址{computer}  {computer.cpu} {computer.disk}')

print('*' * 150)

# 类的浅拷贝 computer2的内存地址不一样了但是里面的类类型的变量地址还是一样的
import copy

computer2 = copy.copy(computer)
print(f'computer2的内存地址{computer2}  {computer2.cpu} {computer2.disk}')
print(f'computer的内存地址{computer}  {computer.cpu} {computer.disk}')

print('*' * 150)
# 类的深拷贝
computer3 = copy.deepcopy(computer)
print(f'computer3的内存地址{computer3}  {computer3.cpu} {computer3.disk}')
print(f'computer的内存地址{computer}  {computer.cpu} {computer.disk}')


