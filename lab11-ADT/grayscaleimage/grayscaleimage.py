from arrays import Array2D


class GrayscaleImage:
    """Represents image"""
    def __init__(self, nrows, ncols):
        #creates 2D array and clear it
        self._img = Array2D(nrows, ncols)
        self._img.clear(0)

    def width(self):
        """Returns width of image"""
        return self._img.num_cols()

    def height(self):
        """Returns height of image"""
        return self._img.num_rows()

    def clear(self, value):
        """Change all pixels to value"""
        self._img.clear(value)

    def __getitem__(self, index_tuple):
        """Returns value of cell"""
        return self._img[index_tuple[0], index_tuple[1]]

    def __setitem__(self, index_tuple, value):
        """Sets cell to value"""
        assert value >=0 and value <= 255, "Incorrect intensity"
        self._img[index_tuple[0], index_tuple[1]] = value

    def __str__(self):
        """Represents image by string"""
        result = ''
        for row in range(self.height()):
            for col in range(self.width()):
                result += str(self[row, col]) + ' '
            result = result[:-1] + '\n'
        return result[:-1]
