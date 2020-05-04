import itertools
from supermark_neu.Station import Station
from supermark_neu.Customer import Customer
import heapq

counter = itertools.count()

# Output Text Declare
Customerdoc = open('supermarkt_customer.txt', 'a')
stationDoc = open('supermarkt_station.txt', 'a')
supermarktDoc = open('supermarkt.txt', 'a')

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
        prio = 3
        if tfunc == leave_station:
            prio = 0
        elif tfunc == arrive:
            prio = 2
        else:
            prio = 1
        heap_info = [time, prio, count, typ_ino, tfunc, order]
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

            time, prio, count, customer, func, order = self.pop_from_queue()

            if func == "begin":
                print(str(time) + " time " + str(time) + " customer " + customer.Name + " " + func)
                m_time, m_func, msg = leave_station(customer, order)
                time = time + m_time
                self.add_to_queue(time, customer, m_func, order)
                print(str(m_time) + " time " + str(time) + " customer " + customer.Name + " " + m_func + " at station " + Stations[order[customer.get_position()]].Name)

            if func == "leave_station":
                m_time, m_func, msg = leave_station(customer, order)
                time = time + m_time
                self.add_to_queue(time, customer, m_func, order)
                print(str(m_time) + " time " + str(time) + " customer " + customer.Name + " " + m_func + " at station " + Stations[order[customer.get_position()]].Name)

            elif func == "arrive":
                m_time, m_func, msg = arrive(customer, order)
                time = time + m_time
                self.add_to_queue(time, customer, m_func, order)
                print(str(m_time) + " time " + str(time) + " customer " + customer.Name + " " + m_func + " at station " + Stations[order[customer.get_position()]].Name)

            elif func == "wait":
                m_time, m_func, msg = wait(customer, order)
                time = time + m_time
                self.add_to_queue(time, customer, m_func, order)

            elif func == "end":
                m_time, m_func, msg = end(customer, order)
                time = time + m_time
                self.add_to_queue(time, customer, m_func, order)
                print(str(m_time) + " time " + str(time) + " customer " + customer.Name + " leaves the supermarket ")

            else:
                leave_supermarket()

            if msg != "":
                Customerdoc.write(str(time) + ":" + msg + "\n")
                Customerdoc.write(str(Stations[0].waiting_queue) + "\n")

        else:
            print("Simulationsende      : " + str(time) + "s", file=supermarktDoc)
            supermarktDoc.write("Simulationsende      : " + str(time) + "s")
            Customerdoc.close()
            stationDoc.close()
            supermarktDoc.close()


def leave_station(customer, order):
    msg = ""
    if customer.get_position() != -1:
        msg = (customer.Name + " Finished at " + Stations[order[customer.get_position()]].Name)
        Stations[order[customer.get_position()]].remove(customer)
    customer.incPosition()
    return customer.walk(), "arrive", msg


def wait(customer, order):
    if Stations[order[customer.get_position()]].isMyTurn(customer.Name):
        zeit, func, msg = service(customer, order)
        return zeit, func, msg
    else:
        return 1, "wait", ""


def arrive(customer, order):
    if customer.get_maximum_wait_time_at_position() > len(Stations[order[customer.get_position()]].waiting_queue):
        msg = (customer.Name + " Queueing at " + Stations[order[customer.get_position()]].Name)
        if Stations[order[customer.get_position()]].is_busy == False:
            Stations[order[customer.get_position()]].add(customer)
            zeit, func, msgtmp = service(customer, order)
            return zeit, func, msg
        else:
            Stations[order[customer.get_position()]].add(customer)
            zeit, func, msgtmp = wait(customer, order)
            return zeit, func, msg
    else:

        msg = (customer.Name + " Dropped at " + Stations[order[customer.get_position()]].Name)
        zeit, func, msgtmp = leave_station(customer, order)
        return zeit, func, msg


def end(customer, order):
    msg = (customer.Name + " Finished at " + Stations[order[customer.get_position()]].Name)
    Stations[order[customer.get_position()]].remove(customer)
    return 0, "leave_supermarket", msg


def leave_supermarket():
    return 0


def service(customer, order):
    if (customer.possible_buying_points() - 1) == customer.get_position():
        msg = (customer.Name + " Buying at " + Stations[order[customer.get_position()]].Name)
        return Stations[order[customer.get_position()]].duration * customer.items_bought[customer.get_position()], "end", msg
    else:
        tmp = Stations[order[customer.get_position()]].duration * customer.items_bought[customer.get_position()]
        return tmp, "leave_station", ""


a = Erignislist()
a.start()
