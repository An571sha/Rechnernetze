import imaplib
import socket
from time import sleep

SEND_HOST = 'alt4.gmail-smtp-in.l.google.com'
SEND_PORT = 25
RECIEVE_PORT = 993


def connect_to_server_and_send_email():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((SEND_HOST, SEND_PORT))
            print(sock.recv(1024))
            sock.send(b"EHLO smtp.gmail.com\r\n")
            print(sock.recv(1024))
            sleep(2)
            # sock.send(b"AUTH PLAIN XHRoYWt1ci5zdXJ5YWRlb0BnbWFpbC5jb21cQW5pbWVzaDIyODcyMDU=\r\n")
            # print(sock.recv(1024))
            sleep(2)
            sock.send(b"MAIL from:<thakur.suryadeo@gmail.com>\r\n")
            print(sock.recv(1024))
            sleep(2)
            sock.send(b"RCPT to:<test@gmail.com>\r\n")
            print(sock.recv(1024))
            sleep(2)
            sock.send(b"DATA\r\n")
            print(sock.recv(1024))
            sleep(2)
            sock.send(b"From: <thakur.suryade@gmail.com>\r\n"
                      b"To: <ozud4n@gmail.com>\r\n "
                      b"Subject: Testing email from socket \r\n"
                      b"This is the body\r\n"
                      b"Adding more lines to the body message.\r\n")
            sock.send(b"\r\n.\r\n")
            print(sock.recv(1024))
    except:
        print("something went wrong")


def connect_to_server_read_inbox():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((SEND_HOST, SEND_PORT))
            print(sock.recv(1024))
            sock.send(b"EHLO imap.gmail.com\r\n")
            print(sock.recv(1024))
    except:
        print("something went wrong")


def connect_using_imap_lib_read_inbox():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login("thakur.suryadeo@gmail.com", "password")
    mail.select('inbox')

    type, data = mail.search(None, 'ALL')
    mail_ids = data[0]
    print(mail_ids)
    print(data)


if __name__ == '__main__':
    connect_using_imap_lib_read_inbox()
