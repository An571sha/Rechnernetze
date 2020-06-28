import threading
import socket

ip = '141.37.168.26'

def portscan(port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    try:
        con = s.connect((ip, port))

        print(f'Port {port} is open')

        con.close()
    except:
        print(f'Port {port} is not open')
        pass

number = 1

for _ in range(1,50):
    t = threading.Thread(target=portscan,kwargs={'port':number})
    number += 1
    t.start()
