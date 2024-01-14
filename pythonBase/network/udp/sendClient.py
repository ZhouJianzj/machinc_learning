from socket import socket, AF_INET, SOCK_DGRAM
# 注意 UDP使用 SOCK_dgram
send = socket(AF_INET, SOCK_DGRAM)
str = input("请输入需要发送的内容！")
send.sendto(str.encode("utf-8"), ('127.0.0.1', 8001))
send.close()
