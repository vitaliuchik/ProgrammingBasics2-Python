class Door:
    def open(self):
        print("Hodor: Closed the door!")

    def open_for_dog(self):
        print("Please, come in!")

class SecureDoor:
    def __init__(self):
        self.door = Door()

    def open(self, login, password):
        if login == "admin" and password == "admin":
            self.door.open()
            print("You open the door!")

sd = SecureDoor()
sd.open("admin", "admin")
sd.open_for_dog()
