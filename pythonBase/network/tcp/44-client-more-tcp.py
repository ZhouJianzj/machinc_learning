from socket import socket

client = socket()
client.connect(('127.0.0.1', 8000))
str = input("请输入你需要想server发送的内容！")
while str != "":
    client.send(str.encode("utf-8"))
    if str == "bye":
        break
    msg = client.recv(1024).decode("utf-8")
    if msg == "bye":
        break
    print(msg)
    str = input("请输入你需要想server发送的内容！")

client.close()
