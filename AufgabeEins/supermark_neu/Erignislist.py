import itertools
from supermark_neu.Station import Station
from supermark_neu.Customer import Customer
import heapq

counter = itertools.count()

Stations = []
Stations.append(Station(10, [], "Bäcker"))
Stations.append(Station(60, [], "Käse"))
Stations.append(Station(30, [], "Metzger"))
Stations.append(Station(5, [], "Kasse"))


class Erignislist:
    heap = []
    typ_one = ([10, 30, 45, 60], [11, 11, 6, 21], [10, 5, 3, 30])
    typ_two = ([30, 30, 20], [6, 21, 21], [2, 3, 3])
    order_one = [0, 2, 1, 3]
    order_two = [2, 3, 0]

    def pop_from_queue(self):
        return heapq.heappop(self.heap)

    def add_to_queue(self, time, typ_ino, tfunc, order):
        count = next(counter)
        heap_info = [time, count, typ_ino, tfunc, order]
        heapq.heappush(self.heap, heap_info)

    def start(self):

        CustomerA1 = Customer(self.typ_one, "T1/K1")
        CustomerB1 = Customer(self.typ_two, "T2/K1")
        CustomerA2 = Customer(self.typ_one, "T2/K2")
        CustomerB2 = Customer(self.typ_two, "T2/K3")
        CustomerB3 = Customer(self.typ_two, "T2/K4")
        CustomerB4 = Customer(self.typ_two, "T1/K2")

        self.add_to_queue(0, CustomerA1, "begin", self.order_one)
        self.add_to_queue(1, CustomerB1, "begin", self.order_two)
        self.add_to_queue(61, CustomerB2, "begin", self.order_two)
        self.add_to_queue(121, CustomerB3, "begin", self.order_two)
        self.add_to_queue(181, CustomerB4, "begin", self.order_two)
        self.add_to_queue(200, CustomerA2, "begin", self.order_one)

        self.event_handler()

    def event_handler(self):
        while self.heap:

            time, count, customer, func, order = self.pop_from_queue()

            if func == "begin":
                print(str(time) + " time " + str(time) + " customer " + customer.Name + " " + func)
                m_time, next_func = self.leave_station(customer, order)
                time = time + m_time
                self.add_to_queue(time, customer, next_func, order)
                print(
                    str(m_time) + " time " + str(
                        time) + " customer " + customer.Name + " " + next_func + " at station " +
                    Stations[order[customer.get_position()]].Name)

            if func == "leave_station":
                m_time, next_func = self.leave_station(customer, order)
                time = time + m_time
                self.add_to_queue(time, customer, next_func, order)
                print(
                    str(m_time) + " time " + str(
                        time) + " customer " + customer.Name + " " + next_func + " at station " +
                    Stations[order[customer.get_position()]].Name)

            elif func == "arrive":
                m_time, next_func = self.arrive(customer, order)
                time = time + m_time
                self.add_to_queue(time, customer, next_func, order)
                print(
                    str(m_time) + " time " + str(
                        time) + " customer " + customer.Name + " " + next_func + " at station " +
                    Stations[order[customer.get_position()]].Name)

            elif func == "wait":
                m_time, next_func = self.wait(customer, order)
                time = time + m_time
                self.add_to_queue(time, customer, next_func, order)

            elif func == "end":
                m_time, next_func = self.end(customer, order)
                time = time + m_time
                self.add_to_queue(time, customer, next_func, order)
                print(str(m_time) + " time " + str(time) + " customer " + customer.Name + " leaves the supermarket ")

            else:
                self.leave_supermarket()

        else:
            print("hehe")

    def arrive(self, customer, order):

        # if customer can wait let him in ---
        if customer.get_maximum_wait_time_at_position() > len(Stations[order[customer.get_position()]].waiting_queue):

            # if station not busy begin with service ---
            if not self.current_station(Stations, customer, order).is_busy:
                self.current_station(Stations, customer, order).add_to_queue(customer)
                time, func = self.service(customer, order)
                return time, func

            # else add him in the the waiting list ---
            else:
                self.current_station(Stations, customer, order).add_to_queue(customer)

                # pop the first waiting customer out ---
                time, func = self.wait(customer, order)
                return time, func

        # else leave the station ---
        else:
            time, func = self.leave_station(customer, order)
            return time, func

    def service(self, customer, order):
        if (customer.possible_buying_points() - 1) == customer.get_position():
            return self.current_station(Stations, customer, order).duration * customer.items_bought[
                customer.get_position()], "end"
        else:
            return self.current_station(Stations, customer, order).duration * customer.items_bought[
                customer.get_position()], "leave_station"

    def leave_station(self, customer, order):
        if customer.get_position() != -1:
            self.current_station(Stations, customer, order).remove(customer)
        customer.incPosition()
        return customer.get_walk_time(), "arrive"

    def wait(self, customer, order):
        if self.current_station(Stations, customer, order).is_current_customer(customer.Name):
            print("here comes service after wait")
            time, func = self.service(customer, order)
            return time, func
        else:
            return 1, "wait"

    def end(self, customer, order):
        self.current_station(Stations, customer, order).remove(customer)
        return 0, "leave_supermarket"

    def leave_supermarket(self):
        return 0

    def current_station(self, stations, customer, order):
        return stations[order[customer.get_position()]]


a = Erignislist()
a.start()
