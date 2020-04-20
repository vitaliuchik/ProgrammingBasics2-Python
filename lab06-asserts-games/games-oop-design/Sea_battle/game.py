import random


class Ship:
    def __init__(self, bow, horizontal, length):
        self.bow = bow
        self.length = length
        self.hit = [False for i in range(length)]
        if horizontal:
            self.positions = [(bow[0] - 1, bow[1] + i - 1) for i in range(length)]
        else:
            self.positions = [(bow[0] + i - 1, bow[1] - 1) for i in range(length)]

    def shoot_at(self, coord):
        self.hit[self.positions.index(coord)] = True
        if False not in self.hit:
            return True
        return False


class Field:
    def __init__(self):
        self.ships = []
        self._generate_field()
        self.past = []
        self.kill_count = 0
        self.shooted = []

    def _generate_field(self):

        def add_ship(field, length):
            # 0 - vertical, 1 - horizontal
            horizontal = random.choice([False, True])
            pos_x = random.randint(0, 9 - length*horizontal)
            pos_y = random.randint(0, 9 - length*(1 - horizontal))
            pos_yx = []
            for y in range(pos_y, pos_y + 1 + (length-1)*(1-horizontal)):
                for x in range(pos_x, pos_x + 1 + (length-1) * horizontal):
                    pos_yx.append((y, x))


            end_y = pos_y + 1 + (length - 1) * (1 - horizontal)
            end_x = pos_x + 1 + (length - 1) * horizontal
            if pos_y != 0:
                start_y = pos_y - 1
            else:
                start_y = pos_y
            if pos_y != 0:
                start_x = pos_x - 1
            else:
                start_x = pos_x
            if end_y == 10:
                end_y = 9
            if end_x == 10:
                end_x = 9
            can_add = True
            for y in range(start_y, end_y + 1):
                for x in range(start_x, end_x + 1):
                    if field[y][x] == 2:
                        can_add = False
            if can_add:
                for y in range(start_y, end_y + 1):
                    for x in range(start_x, end_x + 1):
                        if (y, x) in pos_yx:
                            field[y][x] = 2
                        else:
                            field[y][x] = 1
                return Ship((pos_y+1, pos_x+1), horizontal, length)
            return None

        field = [[0 for i in range(10)] for j in range(10)]
        ship4, ship3, ship2, ship1 = 0, 0, 0, 0
        while ship4 != 1:
            ship = add_ship(field, 4)
            if ship:
                self.ships.append(ship)
                ship4 += 1
        while ship3 != 2:
            ship = add_ship(field, 3)
            if ship:
                self.ships.append(ship)
                ship3 += 1
        while ship2 != 3:
            ship = add_ship(field, 2)
            if ship:
                self.ships.append(ship)
                ship2 += 1
        while ship1 != 4:
            ship = add_ship(field, 1)
            if ship:
                self.ships.append(ship)
                ship1 += 1


    def _take_ship(self, coord):
        for ship in self.ships:
            if coord in ship.positions:
                return ship
        return -1

    def shoot_at(self, coord):
        coord = (coord[0] - 1, coord[1] - 1)
        if coord in self.shooted:
            return 'Already shooted'
        self.shooted.append(coord)
        if self._take_ship(coord) == -1:
            self.past.append(coord)
            return 'past'
        else:
            ship = self._take_ship(coord)
            if not ship.shoot_at(coord):
                return 'injure'
            else:
                self.kill_count += 1
                return 'kill'


class Player:

    def __init__(self, own_field, enemy_field):
        self.own_field = own_field
        self.enemy_field = enemy_field

    def get_own_field(self):
        field = self.own_field
        field._field = [[' ' for i in range(10)] for j in range(10)]
        for ship in field.ships:
            for i in range(ship.length):
                if ship.hit[i]:
                    field._field[ship.positions[i][0]][ship.positions[i][1]] = 'X'
                else:
                    field._field[ship.positions[i][0]][ship.positions[i][1]] = 'O'
        for past_coord in field.past:
            field._field[past_coord[0]][past_coord[1]] = '-'
        result = ''
        for i in range(10):
            result += str(field._field[i]) + '\n'
        return result

    def get_enemy_field(self):
        field = self.enemy_field
        field._field = [[' ' for i in range(10)] for j in range(10)]
        for ship in field.ships:
            for i in range(ship.length):
                if ship.hit[i]:
                    field._field[ship.positions[i][0]][ship.positions[i][1]] = 'X'
        for past_coord in field.past:
            field._field[past_coord[0]][past_coord[1]] = '-'
        result = ''
        for i in range(10):
            result += str(field._field[i]) + '\n'
        return result




