class AcademicBuilding():
    """Represents classroom by address and number of classrooms"""

    def __init__(self, address, classrooms):
        """ Initializes building characteristics"""
        self.address = address
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


    def total_equipment(self):
        """ (AcademicBuildings) -> list
        Returns equipment from all building"""

        equipment = []
        for room in self.classrooms:
            equipment.extend(room.equipment)

        all_equipment = dict()
        for item in equipment:
            all_equipment[item] = all_equipment.get(item, 0)
            all_equipment[item] += 1 
        return list(all_equipment.items())

        
        