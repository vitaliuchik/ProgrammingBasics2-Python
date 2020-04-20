import random
from animal_2 import Bear, Fish

class River:
    """Represents river (ecosystem)"""

    def __init__(self, length):
        # initialization
        self.length = length
        self.river = []
        objs = [Bear, Fish, None]
        for i in range(length):
            obj = random.choice(objs)
            if obj:
                self.river.append(obj())
            else:
                self.river.append(None)


    def __str__(self):
        """String representation of the river"""
        result = ''
        for cell in self.river:
            if cell:
                result += cell.__class__.__name__[:1]
                result += str(cell.power)[:4]
                if cell.gender:
                    result += 'M'
                else:
                    result += 'F'
            else:
                result += ' ' * 6
        return result

    def update_river(self):
        """Updates the river for one year"""
        for i in range(self.length):
            if self.river[i]:
                move = random.randint(-1, 1)
                if move == -1:
                    if i != 0:
                        change_to_none = self._update_cell(i-1, self.river[i])
                        if change_to_none:
                            self.river[i] = None 
                elif move == 1:
                    if i != self.length - 1:
                        change_to_none = self._update_cell(i+1, self.river[i])
                        if change_to_none:
                            self.river[i] = None


    def _update_cell(self, cell, animal):
        """Makes changes, handles meetings of animals in one cell"""
        if not self.river[cell]:
            self.river[cell] = animal
        else:
            if isinstance(self.river[cell], Fish) and \
            isinstance(animal, Bear):
                self.river[cell] = animal

            elif self.river[cell].__class__ == animal.__class__:
                if self.river[cell].gender != animal.gender:
                    self._insert_animal(animal.__class__)
                    return False
                else:
                    if self.river[cell].power < animal.power:
                        self.river[cell] = animal
        return True


    def _insert_animal(self, animal):
        """Inserts defined animal in empty cell, if last exists"""
        none_number = self.length - self.number_animal('Bear') - \
            self.number_animal('Fish')
        if none_number > 0:
            pos = random.randint(1, none_number)
            none_count = 0
            for i in range(self.length):
                if not self.river[i]:
                    none_count += 1
                    if none_number == none_count:
                        self.river[i] = animal()
                        break


    def number_animal(self, animal):
        """Returns number of defined animals"""
        count = {'Bear': 0, 'Fish': 0}
        for cell in self.river:
            if cell:
                if cell.__class__.__name__ == animal:
                    count[animal] += 1
        return count[animal]

