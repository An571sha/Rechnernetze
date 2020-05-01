from supermarkt.Station import Station
from supermarkt.Customer import Customer
import heapq


class Erignislist:
    def __init__(self, time, eventnumber):
        self.heapq = []
        self.time = time
        self.number = eventnumber

        self.begin_event = 'B'
        self.arrive_event = 'A'
        self.leave_event = 'V'

        self.start_simulation(0, 200, self.time, "A")
        self.start_simulation(1, 60, self.time, "B")

        self.baecker = Station('Bäcker', 10)
        self.wursttheke = Station('Metzger', 30)
        self.kaesetheke = Station('Käse', 60)
        self.kasse = Station('Kasse', 5)

    def pop(self):
        return heapq.heappop(self.heapq)

    def push(self, event):
        heapq.heappush(self.heapq, event)

    def start_simulation(self, initial_time, start_time, time_elapsed, typ):
        t = initial_time
        priority = 0
        customer_id = 1

        while t < time_elapsed:
            self.push((t, priority, self.begin_event, Customer(typ + str(customer_id))))
            t += start_time
            customer_id += 1

    def start(self):
        while self.heapq:
            # keeping popping from the list till the list is empty or all events are complete
            time, prio, event, customer = self.pop()

            if event == self.begin_event:

                # Begin the Simulation AND add a arrive event(A) at position 0
                self.push((time + customer.tasks[0][0], 2, 'A0', customer))

            elif event[0] == self.arrive_event:

                position = int(event[1])

                if customer.name[0] == 'A':

                    if position == 0:
                        self.customer_arrive(time, position, customer, self.baecker)
                    elif position == 1:
                        self.customer_arrive(time, position, customer, self.wursttheke)
                    elif position == 2:
                        self.customer_arrive(time, position, customer, self.kaesetheke)
                    else:
                        self.customer_arrive(time, position, customer, self.kasse)
                else:

                    if position == 0:
                        self.customer_arrive(time, position, customer, self.wursttheke)
                    elif position == 1:
                        self.customer_arrive(time, position, customer, self.kasse)
                    else:
                        self.customer_arrive(time, position, customer, self.baecker)

            elif event[0] == self.leave_event:

                position = int(event[1])

                if customer.name[0] == 'A':

                    if position == 0:
                        self.customer_leave(time, position, customer, self.baecker)
                    elif position == 1:
                        self.customer_leave(time, position, customer, self.wursttheke)
                    elif position == 2:
                        self.customer_leave(time, position, customer, self.kaesetheke)
                    else:
                        self.customer_leave(time, position, customer, self.kasse)
                else:

                    if position == 0:
                        self.customer_leave(time, position, customer, self.wursttheke)
                    elif position == 1:
                        self.customer_leave(time, position, customer, self.kasse)
                    else:
                        self.customer_leave(time, position, customer, self.baecker)

    def customer_arrive(self, time, position, customer, station):
        # if the queue length bigger then  max waiting time, leave
        if len(station.queue) >= customer.tasks[position][1]:
            if position < len(customer.tasks) - 1:
                # if not at the last station. go to the next one
                self.push((time + customer.tasks[position + 1][0], 2, self.arrive_event + str(position + 1), customer))
            customer.action(time, 'dropped', station)

        else:
            station.action(time, 'adding', customer)
            station.queue.append((customer, position))
            if not station.is_busy:
                station.is_busy = True
                station.action(time, 'serving', customer)
                station.queue.pop(0)
                customer.action(time, 'Queueing', station)
                self.push((time + station.worktime * customer.tasks[position][2], 1, self.leave_event + str(position),
                           customer))
            else:
                customer.action(time, 'Queueing', station)

    def customer_leave(self, time, position, customer, station):
        customer.action(time, 'Finished', station)
        station.action(time, 'Finished', customer)
        if position < len(customer.tasks) - 1:
            self.push((time + customer.tasks[position + 1][0], 2, self.arrive_event + str(position + 1), customer))
        if station.queue:
            next_customer, n_position = station.queue.pop(0)
            station.action(time, 'serving', next_customer)
            self.push(
                (time + next_customer.tasks[n_position][2] * station.worktime, 1, self.leave_event + str(n_position),
                 next_customer))
        else:
            station.is_busy = False


if __name__ == "__main__":
    my_events = Erignislist(2000, 100000)
    my_events.start()
