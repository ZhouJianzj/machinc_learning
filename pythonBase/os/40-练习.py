# 模拟客服的自动回复

# 读取回复内容文件
def read_answer_file(msg):
    with open("zhoujian.txt", 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if line == "":
                break
            question = line.split(":")[0]
            if question in msg:
                return line.split(":")[1]
    # 都没有匹配到就返回false
    return False


if __name__ == '__main__':
    msg = input("亲!有什么问题需要解决吗!我可以帮助你解决 订单 物流 账户 支付问题:")
    while True:
        if msg == 'bye!':
            break
        result = read_answer_file(msg)
        if not result:
            msg = input("你输入的问题不在我能力范围之内!!!!亲!还有什么问题需要问!!!")
        else:
            print(result)
            msg = input("亲!还有什么问题需要问!!!")
