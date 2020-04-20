class Animal:
    def animate(self, tup):
        self.move_x(tup[0])
        self.move_y(tup[1])

class Dog(Animal):
    def move_x(self, x):
        print("Moved horizontally by %d with speed 10" % x)

    def move_y(self, y):
        print("Moved vertically by %d with speed 10" % y)


class Cat(Animal):
    def move_x(self, x):
        print("Moved horizontally by %d with speed 20" % x)

    def move_y(self, y):
        print("Moved vertically by %d with speed 20" % y)

d = Dog()
d.animate((10,10))
c = Cat()
c.animate((20,20))
