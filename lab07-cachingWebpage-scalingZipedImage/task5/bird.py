class Bird:

    def __init__(self, name):
        self.name = name
        self.eggs = 0

    def __repr__(self):
        egg_str = 'eggs'
        if self.eggs == 1:
            egg_str = 'egg'
        return '{} has {} {}'.format(self.name, self.eggs, egg_str)

    def fly(self):
        return "I can fly!"

    def layEgg(self):
        self.eggs += 1

    def countEggs(self):
        return self.eggs


class Penguin(Bird):

    def fly(self):
        return "No flying for me."

    def swim(self):
        return "I can swim!"


class MessengerBird(Bird):

    def __init__(self, name, message=""):
        super().__init__(name)
        self.message = message

    def deliverMessage(self):
        return self.message
    
    