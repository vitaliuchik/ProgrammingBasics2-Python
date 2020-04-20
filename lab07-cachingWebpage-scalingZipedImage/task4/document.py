from cursor import Cursor
from character import Character


class Document:
    """Represents document"""
    def __init__(self):
        """Initializes variables"""
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''

    def insert(self, character):
        """Insert character on cursor's position 
        (limitations described in document_test.py)"""
        if not hasattr(character, 'character'):
            character = Character(character)
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    def delete(self):
        """Delete character on cursor's position 
        (limitations described in document_test.py)"""
        del self.characters[self.cursor.position]

    def save(self):
        """Save file
        but we should input filename in __init__()"""
        f = open(self.filename, 'w')
        f.write(''.join(self.characters))
        f.close()

    @property
    def string(self):
        "Returns string of characters"
        return ''.join((str(c) for c in self.characters))