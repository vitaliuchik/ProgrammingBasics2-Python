class Field:
    def __init__(self):
        self.ships = []

    @staticmethod
    def generate_field():
        fl = Field()

        pass
        pass
        pass

        return fl

print(Field())
print(Field.generate_field())

class Flower:
    pass

class Bouquet:
    def __init__(self):
        self.flowers = []

    @staticmethod
    def quick_compose(tp):
        if tp == "WEDDING":
            bqt = Bouquet()
            bqt.flowers.append(Flower())
            bqt.flowers.append(Flower())
            bqt.flowers.append(Flower())
        elif tp == "PRESENT":
            bqt = Bouquet()
            bqt.flowers.append(Flower())
        return bqt

bqt = Bouquet()
bqt.quick_compose("WEDDING")

