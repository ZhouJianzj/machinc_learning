# 文件操作


def writeFile():
    # 打开或创建文件
    file = open("zj.txt", 'w', encoding='utf-8')
    # 写操作
    file.write("你好周健")
    # 关闭文件
    file.close()


def readFile():
    # 打开或者创建文件
    file = open('zj.txt', 'r', encoding='utf-8')
    # 读操作
    s = file.read()
    print(s)
    # 关闭文件
    file.close()


"""
追加写
"""


def write_file_append_file(file, str):
    f = open(file, 'a', encoding='utf-8')
    f.write(str)
    f.close()


"""
以list的方式去写
"""


def writ_file_append_list(file, lst):
    f = open(file, 'a', encoding='utf-8')
    f.writelines(lst)
    f.close()


"""
指定读和读取行
"""


def read_file_seek_line_lines():
    f = open('zj.txt', 'r+', encoding='utf-8')
    print('读取全部-------', f.read())
    print("*" * 150)
    # 让指针回到文件开头，utf-8 每个汉字占据3个字节，里面的参数是字节数
    f.seek(0)
    print('读取指定字符个数------', f.read(2))
    f.seek(0)
    print('读取一行中的第几个字符-----', f.readline(1))
    f.seek(0)
    print('读取一整行-------', f.readline())
    f.seek(0)
    print('读取指定行-------', f.readlines(1))
    f.seek(0)
    print("读取所有行返回一个列表，每一行为列表中的一个元素--------", f.readlines())
    f.close()


"""
 使用with 实现文件复制
"""


def opt_file_with():
    # 使用with 就不需要处理一些异常以及关闭操作了
    with open('zj.txt', 'r', encoding='utf-8') as file:
        with open('copy_zj.txt', 'w', encoding='utf-8') as copy_file:
            copy_file.write(file.read())


# 一维数据的读写
def file_csv():
    lst = ['张三', '王五', '李四']
    with open('student.csv', 'w+', encoding='utf-8') as file:
        file.write(','.join(lst))


# 二位数据的读写
def write_file_two():
    lst = [
        ['名称', '价格', '数量'],
        ['小米', '1999', '11'],
        ['华为', '3999', '1']
    ]
    with open('readTwo.txt', 'w+', encoding='utf-8') as file:
        for item in lst:
            file.write(','.join(item))
            file.write('\n')


def read_file_two():
    with open('readTwo.txt', 'r+', encoding='utf-8') as file:
        data = []
        lst = file.readlines()
        for item in lst:
            el = item[:len(item) - 1].split(',')
            data.append(el)
    print(data)


import json


# 高维数据的处理
def json_opt_dumps():
    lst = [
        {'name': '张三', 'age': 12},
        {'name': '李四', 'age': 12},
        {'name': '王五', 'age': 12},
    ]
    # ensure_ascii 表示是否是启用ascii编码，ident 确保json格式的美化
    data = json.dumps(lst, ensure_ascii=False, indent=True)
    return data


def json_opt_file():
    lst = [
        {'name': '张三', 'age': 12},
        {'name': '李四', 'age': 12},
        {'name': '王五', 'age': 12},
    ]
    # ensure_ascii 表示是否是启用ascii编码，ident 确保json格式的美化
    data = json.dumps(lst, ensure_ascii=False, indent=True)
    # 方式一 将json格式的str存入文件
    with open('json.json', 'w+', encoding='utf-8') as file:
        file.write(data)
        print("方式一 将json格式的str存入文件")
    # 方式二
    json.dump(lst, open('json.json', 'w+', encoding='utf-8'), ensure_ascii=False, indent=True)
    print("方式二 将json格式的str存入文件")

    # 方式一加载json格式的文件
    with open('json.json', 'r+', encoding='utf-8') as file:
        json_data = file.read()
        json_data_format = json.loads(json_data)
        print('方式一', type(json_data_format), json_data_format)
    #     方法二
    data_json = json.load(open('json.json', encoding='utf-8'))
    print('方法二', type(data_json), data_json)


if __name__ == '__main__':
    # writeFile()
    # readFile()
    # write_file_append_file('zj.txt', "\n你好")
    # list中元素需要是字符串
    # lst = ['1', '2']
    # writ_file_append_list('zj.txt', lst)
    # read_file_seek_line_lines()
    # opt_file_with()
    # file_csv()

    # write_file_two()
    # read_file_two()

    # 转存list为json格式的str
    # data = json_opt_dumps()
    # print(type(data), data)
    # 将json格式的str加载为list
    # data = json.loads(data)
    # print(type(data), data)

    json_opt_file()
