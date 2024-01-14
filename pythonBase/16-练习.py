# 购物车案例
d = {}
for item in range(2):
    input_value = input("商品请入库（编号 空格 商品名称）：")
    lst = input_value
    num = lst[:lst.index(' ')]
    name = lst[lst.index(' ') + 1:]
    d.update({num: name})

shopping = []
print(d)
while True:
    input_value = input("请输入你选购的商品编号！取消选购请按 q")
    if input_value in d.keys():
        shopping.append(input_value + ":" + d.get(input_value))
    else:
        if input_value == 'q':
            break
        print("你选购的商品不存在！")
print("-" * 40)
print("你选购的商品为", shopping)
