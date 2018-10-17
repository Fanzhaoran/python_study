# 模拟服务器端

import socket

def serverFunc():
    print("服务器端")
    #1 建立soket
    #socket.AF_INET:使用ipv4协议
    #socket.SOCK_DGRAM)：使用UDP通讯
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #2 绑定IP和port

    addr = ("127.0.0.1",7851)
    sock.bind(addr)

    #接受对方的消息

    #rst = sock.recvfrom(500)

    data,addr = sock.recvfrom(500)

    #解码
    print(data)
    print(type(data))

    text = data.decode()
    print(text)
    print(type(text))


    rsp = "I am not hugry"
    data = rsp.encode()  #机器之间传递的是byte

    sock.sendto(data,addr)

if __name__ == '__main__':
    print("server start")
    serverFunc()
    print("end server")
