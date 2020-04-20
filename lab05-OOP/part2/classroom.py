class Classroom():
    """Represents classroom using number, capacity and available equipment"""

    def __init__(self, number, capacity, equipment):
        """ Initializes classroom characteristics"""

        self.number = number
        self.capacity = capacity
        self.equipment = equipment


    def __str__(self):
        """ (Classroom) -> str
        Returns the string representation of the classroom for printing"""

        return 'Classroom {} has a capacity of {} \
persons and has the following equipment: {}.'\
                .format(self.number, self.capacity, ', '.join(self.equipment))


    def __repr__(self):
        """  (Classroom) -> str
        Returns the string representation of the classroom"""

        return "Classroom('{}', {}, {})".format( \
        self.number, self.capacity, self.equipment)


    def is_larger(self, classroom):
        """ (Classroom, Classroom) -> bool
        Compares capacity of two classrooms"""

        return True if self.capacity > classroom.capacity else False


    def equipment_differences(self, classroom):
        """(Classroom, Classroom) -> list
        Returns equipments that are in the first classroom, but not in the second"""
        return list(set(self.equipment) - set(classroom.equipment))

    

