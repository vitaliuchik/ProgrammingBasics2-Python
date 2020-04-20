import random
from animal_3 import Bear, Fish, Otter

class River:
    """Represents river (ecosystem)"""

    def __init__(self, length):
        # initialization
        self.length = length
        self.river = []
        self.posterity = {'Fish': 7, 'Otter': 3, 'Bear': 2}
        self.years = {'Fish': 5, 'Otter': 12, 'Bear': 10}
        objs = [Bear, Fish, Otter, None]
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
                result += str(cell.age)
                if cell.age < 10:
                    result += ' '
            else:
                result += ' ' * 8
        return result

    def update_river(self):
        """Updates the river for one year"""
        for i in range(self.length):
            if self.river[i]:
                self.river[i].age += 1        
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
        for i in range(self.length):
            if self.river[i]:
                if self.river[i].age >= \
                    self.years[self.river[i].__class__.__name__]:
                    self.river[i] = None


    def _update_cell(self, cell, animal):
        """Makes changes, handles meetings of animals in one cell"""
        if not self.river[cell]:
            self.river[cell] = animal
        else:

            if isinstance(self.river[cell], Fish) and \
            (isinstance(animal, Bear) or isinstance(animal, Otter)):
                self.river[cell] = animal

            elif isinstance(self.river[cell], Otter) and \
            isinstance(animal, Bear):
                self.river[cell] = animal

            elif self.river[cell].__class__ == animal.__class__:
                if self.river[cell].gender != animal.gender:
                    for i in range(self.posterity[animal.__class__.__name__]):
                        self._insert_animal(animal.__class__)
                    return False
                else:
                    if self.river[cell].power < animal.power:
                        self.river[cell] = animal
                    elif self.river[cell].power == animal.power:
                        if self.river[cell].age > animal.age:
                            self.river[cell] = animal
        self._remove_animals()
        return True


    def _insert_animal(self, animal):
        """Inserts defined animal in empty cell, if last exists"""
        none_number = self.length - self.number_animal('Bear') - \
            self.number_animal('Fish') - self.number_animal('Otter')
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
        count = {'Bear': 0, 'Fish': 0, 'Otter': 0}
        for cell in self.river:
            if cell:
                if cell.__class__.__name__ == animal:
                    count[animal] += 1
        return count[animal]


    def _find_extreme(self, animal):
        """Finds the younger and the oldest animal of chosen type"""
        min_age, max_age = {'pos': 0, 'age': 0}, {'pos': 0, 'age': 0}
        for i, cell in enumerate(self.river):
            if cell:
                if cell.__class__.__name__ == animal:
                    if cell.age < min_age['age']:
                        min_age['pos'] = i
                    if cell.age > max_age['age']:
                        max_age['pos'] = i
        # if all ages are the same - looking for 
        # next not empty position
        if min_age['pos'] == max_age['pos']:
            k = 0
            for i, cell in enumerate(self.river):
                if cell:
                    if cell.__class__.__name__ == animal:
                        if k == 1:
                            max_age['pos'] = i
                            break
                        else:
                            k += 1
        return (min_age['pos'], max_age['pos'])



    def _remove_animals(self):
        """Checks persent of animals of each type and 
        remove some of them if persent id bigger than 60"""
        bears = self.number_animal('Bear')
        fish = self.number_animal('Fish')
        otters = self.number_animal('Otter')
        animal = None
        if bears / self.length > 0.6:
            animal = 'Bear'
        elif fish / self.length > 0.6:
            animal = 'Fish'
        elif otters / self.length > 0.6:
            animal = 'Otter'
        if animal:
            while self.number_animal(animal) / self.length > 0.6:
                pos1, pos2 = self._find_extreme(animal)
                self.river[pos1] = None
                self.river[pos2] = None
