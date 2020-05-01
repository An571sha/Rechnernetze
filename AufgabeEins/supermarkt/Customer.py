class Customer:
    def __init__(self, name):
        self.name = name
        if name[0] == "A":
            self.tasks = list([(10, 10, 10), (30, 10, 5), (45, 5, 3), (60, 20, 30)])
        elif name[0] == "B":
            self.tasks = list([(30, 5, 2), (30, 20, 3), (20, 20, 3)])

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