class Board:
    def __init__(self, board_type):
        self.board_type = board_type


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Colours:
    def __init__(self, board):
        self.board = board
        if board.board_type == 'fourth':
            self.colours = ['white', 'black']
        elif board.board_type == 'first':
            self.colours = ['white', 'black', 'brown']


class Piece(Colours):

    def __init__(self,piece_type, board_type, colour, x, y ):
        super().__init__(Board(board_type))
        self.board_type = board_type
        self.piece_type = piece_type
        self.x = Position(x, y).x
        self.y = Position(x, y).y
        if colour in self.colours:
            self.colour = colour

    def __str__(self):
        return "The {} {} has location {} on the {} board".format(
            self.colour, self.piece_type, str(self.x)+str(self.y), self.board_type)





if __name__ == '__main__':
    pawn = Piece('pawn', 'first', 'white', 'a', 4)
    print(pawn)