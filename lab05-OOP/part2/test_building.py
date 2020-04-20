import building
import classroom

if __name__ == '__main__':
    classroom1 = classroom.Classroom('012', 12, ['TV', 'printer', 'scanner'])
    classroom2 = classroom.Classroom('008', 80, ['TV', 'PC', 'printer'])
    classroom3 = classroom.Classroom('028', 28, ['projector'])
    building1 = building.AcademicBuilding('Kozelnytska 2a', \
                [classroom1, classroom2, classroom3])

    # a
    print(building1.address)
    for room in building1.classrooms:
        print(room)
    # b
    print(building1.total_equipment())
    # c
    print(building1)