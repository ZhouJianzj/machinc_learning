# 模拟售票 使用prettytable
import datetime

import prettytable as pt


def show_ticket():
    table = pt.PrettyTable()
    lst = [item for item in range(1, 6)]
    lst.insert(0, '行号')
    table.field_names = lst
    for index in range(1, 6):
        cells = ["有票" for row in range(1, 6)]
        cells.insert(0, f'第{index}行')
        table.add_row(cells)
    print(table)


def sell_ticket(row, column):
    table = pt.PrettyTable()
    lst = [item for item in range(1, 6)]
    lst.insert(0, '行号')
    table.field_names = lst
    for index in range(1, 6):

        cells = ["有票" for row in range(1, 6)]
        cells.insert(0, f'第{index}行')
        if row == index:
            cells[column] = "已售"
        table.add_row(cells)
    print(table)


def computed_data_time():
    startDate = input("请输入起始时间：2008-2-12 ")
    day = input("需要推算的时间：15")
    date = datetime.datetime.strptime(startDate, "%Y-%m-%d")
    return date + datetime.timedelta(int(day))


if __name__ == '__main__':
    # show_ticket()
    # set = eval(input("请输入你的购买作为行号和列号！"))
    # print(set)
    # sell_ticket(set[0],set[1])
    print(computed_data_time())
