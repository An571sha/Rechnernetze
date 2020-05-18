class Station:

    def __init__(self, name, worktime, number):
        self.name = name
        self.worktime = worktime
        self.number = number
        self.queue = []
        self.is_busy = False

    def add_queue(self, customer):
        self.queue.append(customer)

    def remove_queue(self):
        self.queue.pop()

    def action(self, time, action, customer):
        with open('supermarkt_station.txt', mode="a") as f:
            text = str(time) + ':' + self.name + ' ' + action + ' customer ' + customer.name + '\n'
            f.write(text)
            f.flush()