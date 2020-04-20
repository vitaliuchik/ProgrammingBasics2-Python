import random


class River:

    def __init__(self, length):
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
        result = ''
        for cell in self.river:
            if isinstance(cell, Bear):
                result += "B"
            elif isinstance(cell, Fish):
                result += "F"
            else:
                result += " "
        return result

    def update_river(self):
        # you can use the code in the comments to control each move
        for i in range(self.length):
            if self.river[i]:
                move = random.randint(-1, 1)
                # print('move: ', move)
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
            # else:
            #     print('move: 0')
            # print(self)


    def _update_cell(self, cell, animal):
        if not self.river[cell]:
            self.river[cell] = animal
        else:
            if isinstance(self.river[cell], Fish) and \
            isinstance(animal, Bear):
                self.river[cell] = animal
            elif isinstance(self.river[cell], Fish) and \
            isinstance(animal, Fish):
                self._insert_animal(Fish)
                return False
            elif isinstance(self.river[cell], Bear) and \
            isinstance(animal, Bear):
                self._insert_animal(Bear)
                return False
        return True


    def _insert_animal(self, animal):
        none_number = str(self).count(' ')
        pos = random.randint(1, none_number)
        none_count = 0
        for i in range(self.length):
            if not self.river[i]:
                none_count += 1
                if none_number == none_count:
                    self.river[i] = animal()
                    break


    def number_animal(self, animal):
        if animal == 'Bear':
            return str(self).count('B')
        else:
            return str(self).count('F')


if __name__ == '__main__':
    # you can use the code in the update_river() comments to control each move
    river1 = River(10)
    print('start:', river1, '\n')
    river1.update_river()
    print('\nresult:', river1)
    print('Bears:', river1.number_animal("Bear"))
    print('Fish:', river1.number_animal("Fish"))
