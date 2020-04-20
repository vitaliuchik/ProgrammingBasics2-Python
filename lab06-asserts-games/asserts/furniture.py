class Furniture:
    """Represents furniture by style and assign"""

    def __init__(self, style, assign):
        """ Initializes furniture characteristics"""
        self.style = style
        self.assign = assign

    def __repr__(self):
        """Returns the string representation of this class"""
        return "<furniture style is {}>".format(self.style)

    def get_assign(self):
        """Returns assign of this furnituure"""
        return self.assign


class Chair(Furniture):
    """Represents chair by style, assign and tipe"""

    def __init__(self, style, assign, tipe):
        """ Initializes chair characteristics"""
        super().__init__(style, assign)
        self.tipe = tipe

    def __repr__(self):
        """Returns the string representation of this class"""
        return "<This {} furniture style is {}>".format(self.tipe, self.style)




if __name__ == '__main__':
    furniture1 = Furniture("empire", "bedroom")
    furniture2 = Furniture("modern", "bathroom")
    assert(not (furniture1 == furniture2))
    assert(furniture1.style == "empire")
    assert(furniture1.assign == "bedroom")
    assert(str(furniture1) == "<furniture style is empire>")
    chair1 = Chair("empire", "bedroom", "armchair")
    assert(chair1.tipe == "armchair")
    assert(isinstance(chair1, Furniture))
    assert(str(chair1) == "<This armchair furniture style is empire>")
    assert(chair1.get_assign() == "bedroom")