import threading
import time

finished = False
arrEv = threading.Event
servEv = threading.Event
QEUETIME = 10
CUSTOMERTIME = 40

class mythread(threading.Thread):

    def customer_thread():
        arrEv.set()
        if servEv.wait(timeout=CUSTOMERTIME):
            servEv.clear()
            return "buyed grocerys"
        servEv.clear()
        return"the queue is to long >.<"

    def station_thread():
        arrEv.wait()
        time.sleep(QEUETIME)
        print("finished with station")
        servEv.set()
        arrEv.clear()

    def main():
        customer = threading.Thread(target=mythread.customer_thread)
        station = threading.Thread(target=mythread.station_thread)

        customer.start()
        station.start()

if __name__ == '__main__':
    mythread.main()
