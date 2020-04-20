class Classroom():
    """Represents classroom using number, capacity and available equipment"""

    def __init__(self, number, capacity, equipment):
        """ Initializes classroom characteristics"""

        self.number = number
        self.capacity = capacity
        self.equipment = equipment

    def __str__(self):
        """ (Student) -> str
        Returns the string representation of the student"""

        return 'Classroom {} has a capacity of {} \
persons and has the following equipment: {}.'\
                .format(self.number, self.capacity, ', '.join(self.equipment))
