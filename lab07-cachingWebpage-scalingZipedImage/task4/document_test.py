from document import Document
from character import Character

d = Document()
d.insert('V')
d.insert('i')
d.insert('t')
d.insert(Character('a', bold=True))
print(d.string)

# a2 - переміщення курсору після кінця файлу - вставляє символ вкінці файлу
# (особливість вбудованої insert, яка використовується),
#  але курсор вже починає відлік від нової позиції
# якщо виконати методи end() або home() після цього - IndexError
d.cursor.end()
d.cursor.forward()
d.insert('i')
print(d.string)
try:
    d.cursor.home()
except IndexError as e:
    print(e)
    d.cursor.back()

# a1 - переміщення курсору перед початком файлу - починає відлік з кінця файлу
# (від'ємні індекси) - якщо індекс "-х" де х >= length(file) 
# - вставляє символ на першу позицію
d.cursor.home()
d.cursor.back()
d.insert('l')
print(d.string)

# b - видалення символу, якого не існує 
# вкінці - list assignment index out of range (Index Error)
# спочатку по аналогії до пункту а - починає видаляти з від'ємних індексів
d.cursor.end()
d.cursor.forward()
try:
    d.delete()
except IndexError as e:
    print(e)
    d.cursor.back()

d.cursor.home()
d.cursor.back()
d.delete()
print(d.string)

# c - збереження файлу без імені
# неможливо передати в цьому модулі, не виправляючи код класів
# виникає FileNotFoundError - при відкритті файлу в методі save

# d - введення декількох символів
# Assertion Error
d.cursor.end()
try:
    d.insert('iy')
except AssertionError:
    print('Assertion Error')
    d.insert('i')
    d.insert('y')
    print(d.string)

