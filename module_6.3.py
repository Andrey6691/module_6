class Horse:

    def __init__ (self):
        super().__init__()
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance

class Eagle:

    def __init__ (self):
        super().__init__()
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance

class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


p1 = Pegasus()

p1.move(0,0)
print(p1.get_pos())
p1.move(10, 20)
print(p1.get_pos())
p1.move(10, 20)
print(p1.get_pos())
p1.voice()
