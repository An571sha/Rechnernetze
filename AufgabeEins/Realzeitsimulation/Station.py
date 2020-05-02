import threading
from threading import Thread, Event
from time import sleep

class Station(Thread):
    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration
        self.queue = []
        self.is_busy = False
        self.arrEv = Event()
        self.servEv = Event()
        self.killEv = Event()
        self.lock = threading.Lock()
        self.DIVISOR = 10

    def run(self):
        while not self.killEv.isSet():
            if self.arrEv.wait(10) is not True:
                continue
            self.is_busy = True
            while len(self.queue) != 0:
                customer = self.queue.pop(0)
                serving_time = customer.current_task.amount * self.duration
                print(f"{self.name} serving customer {customer} for {serving_time} seconds")
                sleep(serving_time//self.DIVISOR)
                customer.servEv.set()
            self.is_busy = False
            self.arrEv.clear()

    def __repr__(self):
        return f"{self.name}"
