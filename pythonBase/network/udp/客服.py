from socket import socket, AF_INET, SOCK_DGRAM

rec = socket(AF_INET, SOCK_DGRAM)
rec.bind(('127.0.0.1', 8001))

while True:
    #  Tuple[bytes, _RetAddress]
    msg, addr = rec.recvfrom(1024)
    print('问题：',msg.decode("utf-8"))
    if msg.decode("utf-8") == "bye":
        rec.sendto(input("回答：").encode('utf-8'), addr)
        break
    rec.sendto(input("回答：").encode('utf-8'),addr)
rec.close()
