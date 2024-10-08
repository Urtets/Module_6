class Horse:

    def __init__(self, x_distance):
        self.x_distance = x_distance
        self.sound = 'Frrr'
        super().__init__(0)

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance


class Eagle:
    sound = 'I train, eat, sleep, and repeat'

    def __init__(self, y_distance):
        self.y_distance = y_distance

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance


class Pegasus(Horse, Eagle):

    def __init__(self):
        super().__init__(0)

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        a = self.x_distance
        b = self.y_distance
        return a, b

    def voice(self):
        print(Eagle.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
