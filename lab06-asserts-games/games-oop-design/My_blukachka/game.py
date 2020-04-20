class Building:

    def __init__(self, building):
        self.building = building
        self.neigh = []
        self.character = None
        self.item = None

    def set_description(self, description):
        self.description = description

    def link_building(self, neigh_building):
        self.neigh.append(neigh_building)

    def set_character(self, character):
        self.character = character

    def set_item(self, item):
        self.item = item

    def get_details(self):
        print(self.building)
        print('--------------------')
        if self.neigh:
            print('You can visit {}.'.format([builds.building for builds in self.neigh]))

    def get_character(self):
        return self.character

    def get_item(self):
        return self.item

    def move(self, building):
        for build in self.neigh:
            if build.building == building:
                return build




class Enemy:

    def __init__(self, name):
        self.name = name
        self.conversation = None
        self.weakness = None
        self.agra = 'enemy'

    def set_conversation(self, conversation):
        self.conversation = conversation

    def set_weakness(self, weakness):
        self.weakness = weakness

    def describe(self):
        print(self.name, 'is here!')

    def talk(self):
        print('[{} says]: {}'.format(self.name, self.conversation))

    def interact(self, item):
        return item == self.weakness

    defeats = 0
    def add_defeat(self):
        Enemy.defeats += 1

    def get_defeated(self):
        return Enemy.defeats


class Friend:

    def __init__(self, name):
        self.name = name
        self.conversation = None
        self.agra = 'friend'

    def set_conversation(self, conversation):
        self.conversation = conversation

    def describe(self):
        print(self.name, 'is here!')

    def talk(self):
        print('[{} says]: {}'.format(self.name, self.conversation))


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



