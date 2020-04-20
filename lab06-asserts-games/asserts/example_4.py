class Door:
    def open(self):
        print("Hodor: Closed the door!")

    def open_for_dog(self):
        print("Please, come in!")

class SecureDoor(Door):
    def open(self, login, password):
        if login == "admin" and password == "admin":
            #super().open()
            print("Yahoo!")

sd = SecureDoor()
sd.open("admin", "admin")
sd.open_for_dog()
