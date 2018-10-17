import socket

#客户端
def clientFunc():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    test = "Are you hugrey"

    data = test.encode()

    sock.sendto(data,("127.0.0.1",7851))  #给服务器端发送消息

    data,addr = sock.recvfrom(200)
    data = data.decode()
    print(test)

if __name__ == '__main__':
    print("客户端开始了")
    clientFunc()
    print("客户端结束了")