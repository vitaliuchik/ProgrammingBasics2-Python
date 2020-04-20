class Flyable:
    def move_x(self, obj, x):
        print("object moved horizontal by " + str(x))
    def move_y(self, obj, y):
        print("object moved vertical by " + str(y))


class Duck:
    def __init__(self, grp):
        self.wings_size = 10
        self.weight = 100
        self.color = "brown"
        self.age = 10
        self.grp = grp

    def move_x(self, x):
        self.grp.move_x(self, x)

    def move_y(self, y):
        self.grp.move_y(self, y)

flb = Flyable()
dck = Duck(flb)
dck.move_x(10)
dck.move_y(20)