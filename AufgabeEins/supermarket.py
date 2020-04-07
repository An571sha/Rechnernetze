import threading
import time

finished = False
arrEv = threading.Event
servEv = threading.Event
QEUETIME = 10
CUSTOMERTIME = 40

def customer_thread():
    while not finished:
        arrEv.set()
        if servEv.wait(timeout=CUSTOMERTIME):
            print("the queue is to long >.<")
            break
        print("buyed grocerys")

def station_thread():
    arrEv.wait()
    time.sleep(QEUETIME)
    print("finished with station")
    servEv.set()

def main():
    customer = threading.Thread(target=customer_thread)
    station = threading.Thread(target=station_thread)

    customer.start()
    station.start()

if __name__ == '__main__':
    main()
