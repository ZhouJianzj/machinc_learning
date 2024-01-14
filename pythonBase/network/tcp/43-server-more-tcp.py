# 先接收客户端连接，后发送消息
from socket import socket, AF_INET, SOCK_STREAM

server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 8000))
server.listen(5)
sendClient, sendInfo = server.accept()
msg = sendClient.recv(1024)
decode_msg = msg.decode("utf-8")
while decode_msg != "":
    if decode_msg == 'bye':
        break
    print(decode_msg)
    str = input("请输入你需要发送给client的内容！")
    if str == 'bye':
        break
    sendClient.send(str.encode('utf-8'))

    decode_msg = sendClient.recv(1024).decode('utf-8')
server.close()
