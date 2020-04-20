class Flyable:
    def move_x(self, x):
        print("this object moved by " + str(x) + " horizontally")

    def move_y(self, y):
        print("this object moved by " + str(y) + " vertically")


class Duck(Flyable):
    def __init__(self):
        self.wings_size = 10
        self.weight = 100
        self.color = "brown"
        self.age = 10

dck = Duck()
dck.move_x(10)
dck.move_y(20)