class Station:

    def __init__(self, name, worktime):
        self.name = name
        self.worktime = worktime
        self.queue = list()
        self.is_busy = False

    def action(self, time, action, customer):
        with open('supermarkt_station.txt', mode="a") as f:
            text = str(time) + ':' + self.name + ' ' + action + ' customer ' + customer.name + '\n'
            f.write(text)
            f.flush()
