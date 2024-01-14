# 服务器端TCP client
from socket import socket, AF_INET, SOCK_STREAM

# 创建客户端
server = socket(AF_INET, SOCK_STREAM)

# 绑定addr port
server.bind(('127.0.0.1',8000))

# 监听port
server.listen(5)
print("服务器启动完毕！等待连接....")
# 接收连接
client_msg = server.accept()
print(client_msg,"连接成功！")
# 接/发数据
msg = client_msg[0].recv(1024)

print(msg.decode(encoding="utf-8"))
# 关闭服务
server.close()

