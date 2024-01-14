import socket

client = socket.socket()
client.connect(("127.0.0.1", 8000))
client.send("你好周健！".encode('utf-8'))
client.close()
