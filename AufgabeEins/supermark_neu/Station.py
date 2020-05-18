class Station:

    def __init__(self, time_taken, queue, name=""):
        self.waiting_queue = queue
        self.Name = name
        self.is_busy = False
        self.duration = time_taken

    def add_to_queue(self, customer):
        self.is_busy = True
        self.waiting_queue.append(customer.Name)

    def is_current_customer(self, customer):
        if self.waiting_queue[0] == customer:
            return True
        return False

    def remove(self, customer):
        if len(self.waiting_queue) == 1 and self.waiting_queue.count(customer.Name) > 0:
            self.is_busy = False
            self.waiting_queue.remove(customer.Name)
        elif len(self.waiting_queue) > 1 and self.waiting_queue.count(customer.Name) > 0:
            self.waiting_queue.remove(customer.Name)
