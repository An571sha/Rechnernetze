import itertools
from heapq import heappush, heappop

# Kunde sollte eine Liste mit 3er Tupel haben,die Tupel beschreiben dann
# 1. Maximal Zeit zum warten
# 2. Gekäufte Menge von Artikel
# 3. ??

counter = itertools.count()


class Customer:
    def __init__(self, name, customer_info):
        self.name = name
        self.position = 0
        self.total_time_spent = customer_info[0]
        self.wait_time_max = customer_info[1]
        self.items_purchased = customer_info[2]


class Station:
    def __init__(self, name, duration_processing, wait_list=[]):
        self.duration_processing = duration_processing
        self.wait_list = wait_list
        self.name = name
        self.is_busy = 0

    def add(self, customer):
        self.wait_list.append(customer)
        self.is_busy = 1

    def remove(self, kunde):
        if (len(self.wait_list)) != 0:
            self.wait_list.remove(kunde)
            self.is_busy = 0


class Events:
    heap = []
    simulation_time = 0
    event_number = 0
    time = 0
    visiting_order = ([0, 2, 1, 3], [0, 1, 2, 3])

    # TODO: add methods - pop, start, calculate total time shopping, waiting and walking

    # stations and customers according to example -
    stations = [Station("Baecker", 10, []),
                Station("Wursttheke", 30, []),
                Station("Kaesetheke", 60, []),
                Station("Kasse", 5, [])]

    # Bäcker - Wursttheke - Käsetheke - Kasse
    customer_type_one = ([10, 30, 45, 60], [10, 10, 5, 20], [10, 5, 3, 30])

    # Wursttheke- Kasse - Bäcker
    customer_type_two = ([30, 30, 20], [5, 20, 20], [2, 3, 3])

    customers = [Customer("chutiya0", customer_type_one),
                 Customer("chutiya1", customer_type_one),
                 Customer("chutiya2", customer_type_one),
                 Customer("chutiya3", customer_type_one),
                 Customer("chutiya4", customer_type_one),
                 Customer("mast0", customer_type_two),
                 Customer("mast1", customer_type_two),
                 Customer("mast2", customer_type_two)]

    def add_events(self, customer, start_time, walking_buying_waiting, visiting_order):
        count = next(counter)
        info_for_heap = [start_time, count, customer, walking_buying_waiting, visiting_order]
        heappush(self.heap, info_for_heap)

    