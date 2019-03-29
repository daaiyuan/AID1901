from socket import *
#设置套接字
s=socket()
# 建立连接
s.connect(("127.0.0.1",8888))

#读取文件
f=open("hua.jpg","rb")
while True:
    data=f.read(1024)
    if not data:
        break
    s.send(data)

f.close()
s.close()
