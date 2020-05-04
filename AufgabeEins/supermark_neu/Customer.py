class Customer:
    def __init__(self, typ_info, name=""):
        self.Name = name
        self.Position = -1
        self.walk_time = typ_info[0]
        self.max_waiting_time = typ_info[1]
        self.items_bought = typ_info[2]

    def possible_buying_points(self):
        return len(self.walk_time)

    def get_position(self):
        return self.Position

    def incPosition(self):
        self.Position += 1

    def walk(self):
        return self.walk_time[self.Position]

    def get_maximum_wait_time_at_position(self):
        if self.Position < self.possible_buying_points():
            return self.max_waiting_time[self.Position]
        else:
            return -1
