class Flower:
    def __init__(self, color, petals, price):
        self.color = color
        self.petals = petals
        self.price = price
    
    def getColor(self):
        return self.color

    def getPetalNum(self):
        return self.petals

    def getPrice(self):
        return self.price

    def __eq__(self, other):
        return self.color == other.color and self.petals == other.petals and \
            self.price == other.price

    def __ne__(self, other):
        return self.color != other.color or self.petals != other.petals or \
            self.price != other.price

                    
class Tulip(Flower):
    def __init__(self, color, petals, price):
        super().__init__(color, petals, price)
        self.type_name = 'Tulip'

    def getType(self):
        return 'Tulip'


class Rose(Flower):
    def __init__(self, color, petals, price):
        super().__init__(color, petals, price)
        self.type_name = 'Rose'


    def getType(self):
        return 'Rose'

class Chamomile(Flower):
    def __init__(self, petals, price):
        self.color = 'white'
        super().__init__('white', petals, price)
        self.type_name = 'Chamomile'

    def lovesMe(self):
        return self.petals % 2 == 1

class FlowerSet:
    def __init__(self, flowers):
        self.flowers = flowers

    def getColors(self):
        colors = [flower.color for flower in self.flowers]
        return set(colors)

    def getPrice(self):
        prices = [flower.price for flower in self.flowers]
        return sum(prices)

    def getFlowers(self):
        fl = [flower.type_name for flower in self.flowers]
        return set(fl)
    
class Bucket:
    def __init__(self, flowers):
        self.flowers = flowers

    def getPrice(self):
        prices = [flower_set.getPrice() for flower_set in self.flowers]
        return sum(prices)

