from arrays import DynamicArray
import random


class IntSet:
    """Represents collection of integer"""

    def __init__(self, n):
        """Initializes IntSet"""
        self._nums = DynamicArray()
        for i in range(n):
            self._nums.append(random.randint(0, 100))

    def __len__(self):
        """Return number of integers"""
        return len(self._nums)

    def __getitem__(self, index):
        """Returns i element of IntSet"""
        return self._nums[index]

    def append(self, item):
        """Add element"""
        self._nums.append(item)

    def _digits(self, num):
        """Returns digits from number"""
        digits = str(num)
        for digit in digits:
            yield int(digit)

    def merge(self, other):
        """Combines two IntSets in one IntSet from digits of their sum
        :param IntSet, IntSet
        :returns InteSet"""
        result = IntSet(0)
        len_first = len(self)
        len_second = len(other)
        if len_first >= len_second:
            for i in range(len_second):
                num = self._nums[i] + other[i]
                for digit in self._digits(num):
                    result.append(digit)
            for i in range(len_second, len_first):
                for digit in self._digits(self._nums[i]):
                    result.append(digit)
        else:
            for i in range(len_first):
                num = self._nums[i] + other[i]
                for digit in self._digits(num):
                    result.append(digit)
            for i in range(len_first, len_second):
                for digit in self._digits(other[i]):
                    result.append(digit)
        return result

    def __str__(self):
        """Represents as string"""
        result = ''
        for i in range(len(self._nums)):
            result += str(self._nums[i]) + ' '
        return result[:-1]
