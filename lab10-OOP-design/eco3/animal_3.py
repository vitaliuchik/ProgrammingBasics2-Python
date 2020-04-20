import random

class Animal:
    """Represents Animal"""
    def __init__(self):
        # initialization
        self.gender = random.choice([True, False])
        self.power = random.random()
        self.age = 0


class Bear(Animal):
    pass


class Fish(Animal):
    pass


class Otter(Animal):
    pass