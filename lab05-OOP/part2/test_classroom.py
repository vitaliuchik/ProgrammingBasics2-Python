import classroom

if __name__ == '__main__':
    classroom1 = classroom.Classroom('012', 12, ['TV', 'printer', 'scanner'])
    classroom2 = classroom.Classroom('008', 80, ['TV', 'PC', 'printer'])
    
    ### 1
    # a
    print(classroom1.number)
    print(classroom1.capacity)
    print(classroom1.equipment)
    # b
    print(classroom1)
    # c
    print(classroom2.is_larger(classroom1)) 
    # d
    print(classroom1.equipment_differences(classroom2))
    # e
    print(repr(classroom1))
    print(repr([classroom1]))
