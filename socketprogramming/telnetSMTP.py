import sys
import telnetlib
import time

tn_ip = "asmtp.htwg-konstanz.de"
tn_username = "rnetin"
tn_password = "ntsmobil"

username = input("Enter username: ")
password = input("Enter password: ")

timeout = 100


def telnet():
    try:
        tn = telnetlib.Telnet(tn_ip)
        tn.write(b"rnetin\n")
        tn.write(b"ntsmobil\n")

    except Exception:
        exc_type, value, traceback = sys.exc_info()
        print("Failed with exception [%s]" % exc_type.__name__)
        print("Unable to connect to Telnet server: " + tn_ip)
        return


def command_line_telnet():
    tn = telnetlib.Telnet(tn_ip)
    time.sleep(10)
    tn.write(b"{}\n".format(username))
    time.sleep(10)
    tn.write(b"{}\n".format(password))
    print("Success!")
    tn.close()


if __name__ == '__main__':
    command_line_telnet()
