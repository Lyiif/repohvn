import socket
import os
def Main():

    host = '46.118.249.220' #Server ip
    print(host)
    port = 4000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    data, addr = s.recvfrom(1024)
    print("spyder is in the web!", str(addr))
    message = input("-> ")
    while message != '!':
        if message != 'q':
            s.sendto(message.encode('utf-8'), addr)
            data, addr = s.recvfrom(1024)
            data = data.decode('utf-8')
            if data != "!":
                print("Message from: " + str(addr))
                print("From connected user: " + data)
                data, addr = s.recvfrom(1024)
                data = data.decode('utf-8')
            message = input("-> ")
        else:
            s.sendto(message.encode('utf-8'), addr)
            s.close()

if __name__=='__main__':
    Main()
