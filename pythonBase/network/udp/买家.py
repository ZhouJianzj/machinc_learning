from socket import socket, AF_INET, SOCK_DGRAM

send = socket(AF_INET, SOCK_DGRAM)
while True:
    send.sendto(input("请输入问题：").encode("utf-8"), ('127.0.0.1', 8001))
    data, addr = send.recvfrom(1024)
    print('回答：', data.decode("utf-8"))
    if data.decode("utf-8") == 'bye':
        send.sendto(input("请输入问题：").encode("utf-8"), ('127.0.0.1', 8001))
        break
send.close()
