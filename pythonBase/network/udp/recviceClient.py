from socket import socket, AF_INET, SOCK_DGRAM

rec = socket(AF_INET, SOCK_DGRAM)
rec.bind(('127.0.0.1', 8001))
#  Tuple[bytes, _RetAddress]
msg, addr = rec.recvfrom(1024)
print(msg.decode("utf-8"))
rec.close()