from supermarkt.Station import Station
from supermarkt.Customer import Customer
import heapq


class EventsList:

    def __init__(self):
        self.total_customers = 0
        self.time_elapsed = 0
        self.queue = []

    def pop(self):
        return heapq.heappop(self.queue)

    def push(self, heap_info):
        heapq.heappush(self.queue, heap_info)


station_list = []

station_list.append(Station("Bäcker", 10, 0))
station_list.append(Station("Käse", 60, 1))
station_list.append(Station("Metzger", 30, 2))
station_list.append(Station("Kasse", 5, 3))

cust_typ_one = ([10, 30, 45, 60], [10, 10, 5, 20], [10, 5, 3, 30], [0, 2, 1, 3])
cust_typ_two = ([30, 30, 20], [5, 20, 20], [2, 3, 3], [2, 3, 0])

C1 = Customer("T1/K1", cust_typ_one)

C2 = Customer("T2/K1", cust_typ_two)

C3 = Customer("T2/K2", cust_typ_two)

C4 = Customer("T2/K3", cust_typ_two)

C5 = Customer("T2/K4", cust_typ_two)

C6 = Customer("T1/K2", cust_typ_one)

# C7 = Customer("T1/K3", cust_typ_one)

# C8 = Customer("T1/K4", cust_typ_one)

events = EventsList()

events.push((0, C1, "begin"))
events.push((1, C2, "begin"))
events.push((61, C3, "begin"))
events.push((121, C4, "begin"))
events.push((181, C5, "begin"))
events.push((200, C6, "begin"))


# events.push((400, C6, "begin"))
# events.push((600, C6, "begin"))


def customer_arrives(time, station, customer):
    if customer.get_which_station() == station.number:

        # print("customer max queue time " + str(customer.max_queuetime[customer.get_position()]))
        # print("customer at station " + str(customer.get_which_station))
        # print("station queue " + str(len(station.queue)))

        if customer.max_queuetime[customer.get_position()] > len(station.queue):
            # print("customer position " + str(customer.get_position()))
            # print("station queue length " + str(len(customer.customer_info) - 1))
            if customer.position < len(customer.station) - 1:
                customer.inc_position()
                print("customer time " + str(customer.walktime[customer.get_position()]))
                print("customer arrived at station " + str(station.name))
                events.push((time + customer.customer_info[customer.get_position()][0], customer, 'arrive' +
                             str(customer.get_position())))

        else:
            station.add_queue(customer)
            if not station.is_busy:
                station.queue.pop(0)
                events.push((time + station.worktime * customer.customer_info[customer.position][2], 1,
                             'leave' + str(customer.position), customer))
    return time


def customer_leaves(time, station, customer):
    if customer.get_which_station() == station.number:
        print("station leave " + str(len(station.queue)))
        if customer.position < len(customer.customer_info) - 1:
            customer.inc_position()
            events.push(
                (time + customer.customer_info[customer.position][0], customer, 'arrive' + str(customer.position)))

        else:
            next_customer = station.queue.pop(0)
            events.push((time + next_customer.tasks[next_customer.position][2] * station.worktime, next_customer,
                         'leave' + str(next_customer.position)))
    return time


def handler(time, customer, event):
    for station in station_list:

        if "begin" in event:

            time = time + customer.walktime[customer.position]
            time = customer_arrives(time, station, customer)

        elif "arrive" in event:

            time = customer_arrives(time, station, customer)

        elif "leave":

            time = customer_leaves(time, station, customer)

    return time


if __name__ == '__main__':
    # add event and all varaiable in a tupel
    while events.queue:
        mtime, mcustomer, mevent = events.pop()
        events.time_elapsed = events.time_elapsed + 1
        events.time_elapsed = handler(mtime, mcustomer, mevent)

    print(events.time_elapsed)
