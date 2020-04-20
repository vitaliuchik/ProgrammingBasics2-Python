class Character:
    """Represents character"""
    def __init__(self, character, bold=False, italic=False, underline=False):
        """Initializes variables, determines if it is only one character"""
        assert len(character) == 1
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        """Represents character for printing"""
        bold = "*" if self.bold else ''
        italic = '/' if self.italic else ''
        underline = '_' if self.underline else ''
        return bold + italic + underline + self.character
