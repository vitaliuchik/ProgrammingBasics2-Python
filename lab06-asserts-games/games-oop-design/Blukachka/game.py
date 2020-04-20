class Room:

    def __init__(self, room):
        self.room = room
        self.description = None
        self.neigh = dict()
        self.character = None
        self.item = None

    def set_description(self, description):
        self.description = description

    def link_room(self, neigh_room, direction):
        self.neigh[direction] = neigh_room

    def set_character(self, character):
        self.character = character

    def set_item(self, item):
        self.item = item

    def get_details(self):
        print(self.room)
        print('--------------------')
        print(self.description)
        if self.neigh:
            for direct in self.neigh.items():
                print('The {} is {}.'.format(direct[1].room, direct[0]))

    def get_character(self):
        return self.character

    def get_item(self):
        return self.item

    def move(self, direction):
        return self.neigh[direction]




class Enemy:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.conversation = None
        self.weakness = None

    def set_conversation(self, conversation):
        self.conversation = conversation

    def set_weakness(self, weakness):
        self.weakness = weakness

    def describe(self):
        print(self.name, 'is here!')
        print(self.description)

    def talk(self):
        print('[{} says]: '.format(self.name, self.conversation))

    def fight(self, item):
        return item == self.weakness

    defeats = 0
    def get_defeated(self):
        Enemy.defeats += 1
        return Enemy.defeats


class Item:

    def __init__(self, name):
        self.name = name
        self.description = None

    def set_description(self, description):
        self.description = description

    def describe(self):
        print('The [{}] is here - {}'.format(self.name, self.description))

    def get_name(self):
        return self.name



