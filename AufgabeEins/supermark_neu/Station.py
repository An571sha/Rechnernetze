class Station:

    def __init__(self, time_taken, queue, name=""):
        self.waiting_queue = queue
        self.Name = name
        self.is_busy = False
        self.duration = time_taken

    def add(self, customer):
        self.is_busy = True
        self.waiting_queue.append(customer.Name)

    def isMyTurn(self, Kundename):
        if (self.waiting_queue[0] == Kundename):
            return True
        return False

    def remove(self, Kunde):
        if (len(self.waiting_queue) == 1 and self.waiting_queue.count(Kunde.Name) > 0):
            self.is_busy = False
            self.waiting_queue.remove(Kunde.Name)
        elif (len(self.waiting_queue) > 1 and self.waiting_queue.count(Kunde.Name) > 0):
            self.waiting_queue.remove(Kunde.Name)
