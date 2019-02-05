import os

port = input('> ')

def killport():

    res = os.popen("lsof -i tcp:{}".format(port))
    print(res)
    print(type(res))


    l = res.readlines()    #因为类型是一个可读性文件所以直接读取

    if len(l)>1:

        print(l[1])
        kill_kid = int(l[1][10:16])   #一般情况占用的端口的位置就这么多，第10-16的字符读取出来
        print(kill_kid)           #为了方便看所以给打印出来

        try:
            os.popen('kill {}'.format(kill_kid))
            print("恭喜你！端口关闭了")

        except:

            print("端口不存在!")

    else:

        print("端口就没有占用！")

if __name__ == '__main__':

    killport()
