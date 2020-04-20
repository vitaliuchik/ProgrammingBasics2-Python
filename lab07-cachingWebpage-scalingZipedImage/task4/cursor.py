class Cursor:
    """Represents cursor"""
    def __init__(self, document):
        """Initializes variables"""
        self.document = document
        self.position = 0

    def forward(self):
        """Move position forward"""
        self.position += 1

    def back(self):
        """Move position back"""
        self.position -= 1

    def home(self):
        """Move cursor to the beginning of the line 
        (limitations described in document_test.py)"""
        while self.document.characters[self.position-1] != '\n':
            self.position -= 1
            if self.position == 0:
                break

    def end(self):
        """Move cursor to the end of the line 
        (limitations described in document_test.py)"""
        while self.position < len(self.document.characters) and self.document.characters[self.position] != '\n':
            self.position += 1
