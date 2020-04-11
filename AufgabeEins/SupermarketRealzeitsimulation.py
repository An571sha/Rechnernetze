import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-1s) %(message)s')

CUSTOMER_TIME = 10
STATION_TIME = 5
event = threading.Event()
arrEv = threading.Event()
lock_station = threading.Lock()
lock_customer = threading.Lock()

queue = []


def customer_thread():
    lock_customer.acquire()
    event.set()
    if arrEv.wait(timeout=CUSTOMER_TIME):
        logging.debug('buyed grocerys')
        arrEv.clear()
        lock_customer.release()
        return
    lock_customer.release()
    arrEv.clear()
    logging.debug('the queue is to long >.<')


def station_thread():
    while True:
        event.wait()
        print("acquire lock")
        lock_station.acquire()
        print("lock acquired")
        time.sleep(STATION_TIME)
        logging.debug('finished with station')
        arrEv.set()
        lock_station.release()
        event.clear()


def main():
    t1 = threading.Thread(name='customer', target=customer_thread)
    t3 = threading.Thread(name='customer', target=customer_thread)
    t2 = threading.Thread(name='station', target=station_thread)
    t1.start()
    t3.start()
    t2.start()


if __name__ == '__main__':
    main()
