import socket
from time import sleep

HOST = 'alt4.gmail-smtp-in.l.google.com'  # The remote host
PORT = 25


def connect_to_server_and_send_email():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            print(sock.recv(1024))
            sock.send(b"EHLO smtp.gmail.com\r\n")
            print(sock.recv(1024))
            sleep(2)
            sock.send(b"MAIL from:<thakur.suryade@gmail.com>\r\n")
            print(sock.recv(1024))
            sleep(2)
            sock.send(b"RCPT to:<ozud4n@gmail.com>\r\n")
            print(sock.recv(1024))
            sleep(2)
            sock.send(b"DATA\r\n")
            print(sock.recv(1024))
            sleep(2)
            sock.send(b"test.\r\n")
            print(sock.recv(1024))
    except:
        print("something went wrong")


if __name__ == '__main__':
    connect_to_server_and_send_email()
