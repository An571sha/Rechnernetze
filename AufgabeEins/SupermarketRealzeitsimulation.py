import threading
import time
import logging
import concurrent.futures

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
    while True:
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


with concurrent.futures.ThreadPoolExecutor() as executor:
    station = executor.submit(station_thread)
    customers = [executor.submit(customer_thread) for _ in range(3)]
