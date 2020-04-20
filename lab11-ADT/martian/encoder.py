import ctypes


class Array :
    # Creates an array with size elements.
    def __init__( self, size ):
        assert size > 0, "Array size must be > 0"
        self._size = size
        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        # Initialize each element.
        self.clear(None)

    # Returns the size of the array.
    def __len__( self ):
        return self._size

    # Gets the contents of the index element.
    def __getitem__( self, index ):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._elements[ index ]

    # Puts the value in the array element at index position.
    def __setitem__( self, index, value ):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._elements[ index ] = value

    # Clears the array by setting each element to the given value.
    def clear( self, value ):
        for i in range( len(self) ) :
            self._elements[i] = value

    # Returns the array's iterator for traversing the elements.
    def __iter__( self ):
        return _ArrayIterator( self._elements )

# An iterator for the Array ADT.
class _ArrayIterator :
    def __init__( self, the_array ):
        self._array_ref = the_array
        self._cur_index = 0

    def __iter__( self ):
        return self

    def __next__( self ):
        if self._cur_index < len( self._array_ref ) :
            entry = self._array_ref[ self._cur_index ]
            self._cur_index += 1
            return entry
        else:
            raise StopIteration


class Encoder:
    """Encodes string into degrees"""
    def __init__(self, message):
        # initializes variables and changes string into degrees
        self._length = len(message)
        self._symbols = Array(2*len(message))
        self._angles = Array(2*len(message))        
        for i in range(len(message)):
            hex_symbols = hex(ord(message[i]))[2:]
            self._symbols[2*i] = hex_symbols[0]
            self._symbols[2*i + 1] = hex_symbols[1]
        self._circle = '0123456789abcdef'

        self._angles[0] =  self._angle_between('0', self._symbols[0])
        for i in range(1, 2*len(message)):
            self._angles[i] = self._angle_between(
                self._symbols[i - 1], self._symbols[i])

    def _angle_between(self, a, b):
        # calculates minimal angle between two hex symbols
        # positive if moving clockwise, negative - anticlockwise
        pos_a = self._circle.index(a)
        pos_b = self._circle.index(b)
        abs_angle = abs(pos_a - pos_b)*22.5
        if abs_angle > 180:
            angle = 360 - abs_angle
            if pos_a < pos_b:
                angle *= -1
        else:
            angle = abs_angle
            if pos_b < pos_a:
                angle *= -1
        if angle == -180:
            angle = 180
        if str(angle)[-2:] == '.0':
            return str(angle)[:-2]
        return str(angle)

    def __len__( self ):
        # Returns the size of the encoder array.
        return 2*self._length

    def __getitem__(self, index):
        # Gets the contents of the index element.
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._angles[index]

    def __str__(self):
        # Represents encoder array in string
        result = '| '
        for i in range(2*self._length):
            result += self._angles[i] + ', '
        return result[:-2] + '|'
