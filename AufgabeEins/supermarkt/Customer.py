class Customer:

    def __init__(self, name, customer_info):
        self.name = name
        self.position = 0
        self.customer_info = customer_info
        self.walktime = customer_info[0]
        self.max_queuetime = customer_info[1]
        self.items_bought = customer_info[2]
        self.station = customer_info[3]

    def get_position(self):
        return self.position

    def inc_position(self):
        self.position += 1

    def get_which_station(self):
        return self.station[self.position]

    def __lt__(self, other):
        return self.name < other.name

    def __gt__(self, other):
        return other.__lt__(self)

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def action(self, time, action, station):
        with open("supermarkt_customer.txt", mode="a") as f:
            text = str(time) + ':' + self.name + ' ' + action + ' at ' + station.name + '\n'
            f.write(text)
            f.flush()
