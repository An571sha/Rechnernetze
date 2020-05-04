import threading
from threading import Thread, Event
import time, datetime

class Customer(Thread):
    def __init__(self, name, tasks):
        Thread.__init__(self)
        self.tasks = list(tasks)
        self.name = name
        self.current_task = self.tasks.pop(0)
        self.skipped_tasks = []
        self.time_start = datetime.datetime.now()
        self.time_end = None
        self.servEv = Event()
        self.DIVISOR = 10

#thread of customer: the customers is searching for his next task; when he arrives at a station, he goes sleeping untill the station is finished and wakes him up
    def run(self):
        print(f"{self.name} {self.time_start.strftime('%X')} is running")
        while self.current_task is not None:
            #time that the customer need to walk between stations
            time.sleep(self.current_task.walking_time // self.DIVISOR)
            station = self.current_task.station
            station.lock.acquire()
            #checks if the queue of the station is too long
            if station.is_busy and len(station.queue) > self.current_task.max_queue_time:
                #if the station is too long, the customer will skip it
                self.skip_task()
                station.lock.release()
                continue
            else:
                #customer lines up at the station
                station.queue.append(self)
                station.arrEv.set()
            station.lock.release()
            print(f"{self.name} is waiting at {station}")
            #customer goes to sleep until the station is finished with the task
            self.servEv.wait()
            #needs to be cleared because set wakes up all customers
            self.servEv.clear()
            self.finish_current_task()
        self.time_end = datetime.datetime.now()
        print(f"{self.name} has finished in {self.time_end.strftime('%X')}")

    def __repr__(self):
        return f"{self.name}"

#if all tasks are finished, the customer will stop
    def finish_current_task(self):
        if len(self.tasks) == 0:
            self.current_task = None
        else:
            self.current_task = self.tasks.pop(0)

#if the queue of a station is too long, the customer will skip it
    def skip_task(self):
        self.skipped_tasks.append(self.current_task)
        self.finish_current_task()
