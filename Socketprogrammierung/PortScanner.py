import sys
import threading
import socket

from past.builtins import raw_input

ip = '141.37.168.26'

def portscanTCP(port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    try:
        con = s.connect((ip, port))

        print(f'TCP Port {port} is open')

        #con.close()
    except socket.error as e:
        print(e)
        #print(f'Port {port} is not open')
        pass

number = 1

def portscanUDP(port):


    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        con = s.connect_ex((ip, port))
        if con == 0:
            r_con = con
        print(f'UDP Port {port} is open')
        #con.close()
    except socket.error as e:
        print(e)
        #print(f'UDP Port {port} is not open')
        pass
    return r_con

# for _ in range(1,50):
#     t = threading.Thread(target=portscanTCP,kwargs={'port':number})
#     u = threading.Thread(target=portscanUDP,kwargs={'port':number})
#     number += 1
#     t.start()
#     u.start()
portscanTCP(37)
#portscanUDP(37)
