from sys import path, stdout
path.append("lib/")
from socket import socket,AF_INET,SOCK_STREAM
from threading import Thread
from lib import Send
from time import sleep

for i in range(100):
    print("/-\|"[i % 4], end="\b")
    stdout.flush()
    sleep(0.1)

def main(tcp,send,host='',port=7000):
    connect=(host,port)
    tcp.bind(connect)
    tcp.listen(1)

    while True:
        con,cliente=tcp.accept()
        print('Cliente ',cliente,' conectado!')
        send.con=con

    while True:
        msg=con.recv(1024)
        if not msg: break
        print(str(msg,'utf-8'))

if __name__ == '__main__':
    tcp=socket(AF_INET,SOCK_STREAM)
    send=Send()
    processo=Thread(target=main,args=(tcp,send))
    processo.start()

    print('Listing connection...')

    msg=input()
    while True:
        send.put(msg)
        msg=input()

    processo.join()
    tcp.close()
    exit()