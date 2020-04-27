import itertools
from heapq import heappush, heappop

counter = itertools.count()


class Customer:
    def __init__(self, name, customer_info):
        self.name = name
        self.position = 0
        self.walking_time = customer_info[0]
        self.wait_time_max = customer_info[1]
        self.items_purchased = customer_info[2]

    def stations_visited(self):
        return len(self.walking_time)

    def walk(self):
        return self.walking_time[self.position]

    def increment_position(self):
        self.position += 1


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


# stations and customers according to example -
stations = [Station("Baecker", 10, []),
            Station("Wursttheke", 30, []),
            Station("Kaesetheke", 60, []),
            Station("Kasse", 5, [])]


class Events:
    heap = []
    simulation_time = 0
    event_number = 0
    time = 0
    visiting_order = ([0, 2, 1, 3], [0, 1, 2, 3])

    # TODO: add methods - pop, start, calculate total time shopping, waiting and walking

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

    def get_events(self):
        zip()


def customer_enters(customer, order):
    if customer.wait_time_max() > len(stations[order[customer.position()]].wait_list):
        if stations[order[customer.position]].is_busy == 0:
            return customer_service(customer, order)
        else:
            return customer_waiting(customer, order)

    else:
        customer.increment_position()
        return customer_walking(customer, order)


def customer_waiting(customer, order):
    # add customer to the station's Waiting List
    stations[order[customer.position()]].add(customer)
    # returns the waiting time
    return len(stations[order[customer.getPosition()]].wait_list) * stations[
        order[customer.getPosition()]].duration_processing, customer_service


def customer_walking(customer, order):
    return customer.walk(), customer_enters


def customer_service(customer, order):
    if (customer.stations_visited - 1) == customer.position:
        return stations[order[customer.position()]].duration_processing * customer.items_purchased[
            customer.position], end
    else:
        tmp = stations[order[customer.position]].duration_processing * customer.items_purchased[customer.getPosition()]
        customer.increment_position()
        return tmp, customer_walking


def end():
    print("end")
    return 0

