class Building():
    """Represents building by address"""
    def __init__(self, address):
        """ Initializes building characteristics"""
        self.address = address


class House(Building):
    """Represents house by address and flats"""
    def __init__(self, address, flats):
        """ Initializes house characteristics"""
        super().__init__(address)
        self.flats = flats


class AcademicBuilding():
    """Represents classroom by address and number of classrooms"""

    def __init__(self, address, classrooms):
        """ Initializes building characteristics"""
        super().__init__(address)
        self.classrooms = classrooms


    def __str__(self):
        """ (AcademicBuilding) -> str
        Returns the string representation of the building and classrooms for printing"""
        
        result = self.address + '\n'
        for room in self.classrooms:
            result += 'Classroom {} has a capacity of {} \
persons and has the following equipment: {}.'\
                .format(room.number, room.capacity, ', '.join(room.equipment)) \
                + '\n'
        return result[:-1] 