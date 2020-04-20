import json


def average(grades):
    sum = 0
    k = 0
    for subject in grades:
        if subject != 'serial':
            sum += grades[subject]
            k += 1
    return (sum/k, grades['serial'])


file = open('training.json', encoding='utf-8')
lines = file.readlines()[1:]
file.close()

serials = []

for line in lines:
    grades = json.loads(line[:-1])
    serials.append(average(grades))

serials.sort(key=lambda x: x[0], reverse=True)

top = {'serials':[]}
for serial in serials:
    if serial[0] == serials[0][0]:
        top['serials'].append(serial[1])
    else:
        break

top = json.dumps(top)
file = open('grade_results.json','w', encoding='utf-8')
file.write(top)
file.close()