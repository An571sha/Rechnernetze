import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-1s) %(message)s')

event = threading.Event()
arrEv = threading.Event()
CUSTOMER_TIME = 10
STATION_TIME = 5


def customer_thread():
    event.set()
    if arrEv.wait(timeout=CUSTOMER_TIME):
        logging.debug('buyed grocerys')
        arrEv.clear()
        return
    arrEv.clear()
    logging.debug('the queue is to long >.<')


def station_thread():
    event.wait()
    time.sleep(STATION_TIME)
    logging.debug('finished with station')
    arrEv.set()
    event.clear()


def main():
    t1 = threading.Thread(name='customer', target=customer_thread)
    t2 = threading.Thread(name='station', target=station_thread)
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()