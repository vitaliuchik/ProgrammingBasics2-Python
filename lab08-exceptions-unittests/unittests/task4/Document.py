class CursorError(Exception):
    def __str__(self):
        return 'CursorError: cursor is out of file.'


class FileNameError(Exception):
    def __str__(self):
        return 'FileNameError: filename is empty.'


class CharacterDeleteError(Exception):
    def __str__(self):
        return "CharacterDeleteError: character doesn't exist."


class CharacterError(Exception):
    def __str__(self):
        return "CharacterError: given 2 characters instead of 1."


class Document:
    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ""

    def insert(self, character):
        if self.cursor.position > len(self.characters) or self.cursor.position < 0:
            raise CursorError
        else:
            if not hasattr(character, "character"):
                character = Character(character)
            self.characters.insert(self.cursor.position, character)
            self.cursor.forward()

    def delete(self):
        if self.cursor.position > len(self.characters) or self.cursor.position < 0:
            raise CharacterDeleteError
        else:
            del self.characters[self.cursor.position]

    def save(self):
        if self.filename == '':
            raise FileNameError
        else:
            with open(self.filename, "w") as f:
                f.write("".join(self.characters))

    @property
    def string(self):
        return "".join((str(c) for c in self.characters))


class Cursor:
    def __init__(self, document):
        self.document = document
        self.position = 0

    def forward(self):
        if self.position >= len(self.document.characters):
            raise CursorError
        else:
            self.position += 1
        

    def back(self):
        if self.position <= 0:
            raise CursorError
        else:
            self.position -= 1

    def home(self):
        while self.document.characters[self.position - 1].character != "\n":
            self.position -= 1
            if self.position == 0:
                # Got to beginning of file before newline
                break

    def end(self):
        while (
            self.position < len(self.document.characters)
            and self.document.characters[self.position].character != "\n"
        ):
            self.position += 1


class Character:
    def __init__(self, character, bold=False, italic=False, underline=False):
        if len(character) != 1:
            raise CharacterError
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        bold = "*" if self.bold else ""
        italic = "/" if self.italic else ""
        underline = "_" if self.underline else ""
        return bold + italic + underline + self.character

if __name__ == '__main__':

    d = Document()
    d.insert('v')
    d.insert('i')

    try:
        d.insert('ta')
    except CharacterError as e:
        print(e)

    d.cursor.position = 3
    try:
        d.delete()
    except CharacterDeleteError as e:
        print(e)
    try:
        d.insert('t')
    except CursorError as e:
        print(e)
    try:
        d.cursor.forward()
    except CursorError as e:
        print(e)

    try:
        d.save()  
    except FileNameError as e:
        print(e)
