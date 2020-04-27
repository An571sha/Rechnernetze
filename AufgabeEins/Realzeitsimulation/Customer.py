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

    def run(self):
        print(f"{self.name} {self.time_start.strftime('%X')} is running")
        while self.current_task is not None:
            time.sleep(self.current_task.walking_time // self.DIVISOR)
            station = self.current_task.station
            station.lock.aquier()
            if station.is_busy and len(station.queue) > self.current_task.max_queue_time:
                self.skip_task()
                station.lock.release()
                continue
            else:
                station.queue.append(self)
                station.arrEv.set()
            station.lock.release()
            print(f"{self.name} is waiting at {station}")
            self.servEv.wait()
            self.servEv.clear()
            self.finish_current_task()
        self.time_end = datetime.datetime.now()
        print(f"{self.name} has finished in {self.time_end.strftime('%X')}")

    def __repr__(self):
        return f"{self.name}"

    def finish_current_task(self):
        if len(self.tasks) == 0:
            self.current_task = None
        else:
            self.current_task = self.tasks.pop(0)

    def skip_task(self):
        self.skipped_tasks.append(self.current_task)
        self.finish_current_task()
