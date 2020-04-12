# Kunde sollte eine Liste mit 3er Tupel haben,die Tupel beschreiben dann
# 1. Maximal Zeit zum warten
# 2. Gekäufte Menge von Artikel
# 3. ??


class Customer:
    def __init__(self, name, customer_info):
        self.name = name
        self.max_wait_time = customer_info[0]
        self.purchased = customer_info[1]
        self.unknown = customer_info[2]


class Station:
    def __init__(self, duration_processing, wait_list=[]):
        self.duration_processing = duration_processing
        self.wait_list = wait_list
        self.is_busy = 0

    def add(self, kunde):
        self.wait_list.append(kunde)
        self.is_busy = 1

    def remove(self, kunde):
        if (len(self.wait_list)) != 0:
            self.wait_list.remove(kunde)
            self.is_busy = 0


class Events:
    heap = []
    simulation_time = 0
    event_number = 0

    # TODO: add methods, push, pop, and start, also add Customers of both type, given in example
