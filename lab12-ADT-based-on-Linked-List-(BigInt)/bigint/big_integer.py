class TwoWayNode:

    def __init__(self, data, previous = None, next = None):
        self.data = data
        self.next = next
        self.previous = previous


class BigInteger:
    """Represents big integers"""
    def __init__(self, initValue = '0'):
        self._int = TwoWayNode(initValue[-1])
        tail = self._int
        for i in range(len(initValue) - 2, -1, -1):
            tail.next = TwoWayNode(initValue[i], tail)
            tail = tail.next
        self._last = tail

    def _append_front(self, value):
        # append symbol at the beginning
        self._last.next = TwoWayNode(value)
        self._last = self._last.next

    def _append_back(self, value):
        # append symbol in the end
        first = TwoWayNode(value)
        first.next = self._int
        self._int = first
    
    def sliced_minus(self):
        # check and remove if number has a minus
        if self.toString()[0] == '-':
            return BigInteger(self.toString()[1:])
        else:
            return BigInteger(self.toString())
    
    def __str__(self):
        result = ''
        prob = self._int
        while prob is not None:
            result += prob.data
            prob = prob.next
        return result[::-1]

    def toString(self):
        return str(self)

    def __len__(self):
        length = 0
        prob = self._int
        while prob is not None:
            length += 1
            prob = prob.next
        return length


    ### logical 
    def help_lt(self, other):
        # x < y
        if len(self) != len(other):
            return len(self) < len(other) 
        else:
            prob_self = self._last
            prob_other = other._last
            while prob_self is not None:
                if int(prob_self.data) != int(prob_other.data):
                    return int(prob_self.data) < int(prob_other.data)
                else:
                    prob_self = prob_self.previous
                    prob_other = prob_other.previous
            return False


    def __lt__(self, other):
        # x < y
        if self._last.data != '-' and other._last.data != '-':
            return self.help_lt(other)
        elif self._last.data == '-' and other._last.data != '-':
            return True
        elif self._last.data != '-' and other._last.data == '-':
            return False
        else:
            return other.sliced_minus().help_lt(self.sliced_minus())

    def __gt__(self, other):
        # x > y
        return other < self

    def __le__(self, other):
        # x <= y
        return self < other or self == other

    def __ge__(self, other):
        # x >= y
        return self > other or self == other
    
    def __eq__(self, other):
        # x == y
        if len(self) == len(other):
            prob_self = self._last
            prob_other = other._last
            while prob_self is not None:
                if int(prob_self.data) == int(prob_other.data):
                    prob_self = prob_self.previous
                    prob_other = prob_other.previous
                else:
                    return False
            return True
        return False

    def __ne__(self, other):
        # x != y
        return self < other or self > other

    
    # arithmetic
    def help_add(self, other):
        """Help function for __add__"""
        prob_self = self._int
        prob_other = other._int
        result = BigInteger()
        result._int.data = ''
        other_part = None
        for i in range(min(len(self), len(other))):
            summ = int(prob_self.data) + int(prob_other.data)
            if other_part:
                summ += other_part
            if summ < 10:
                result = BigInteger(result.toString() + str(summ))
                other_part = None
            else:
                result = BigInteger(result.toString() + str(summ)[1])
                other_part = int(str(summ)[0])
            prob_self = prob_self.next
            prob_other = prob_other.next
        if len(self) > len(other):
            for i in range(len(other), len(self)):
                summ = int(prob_self.data)
                if other_part:
                    summ += other_part
                if summ < 10:
                    result = BigInteger(result.toString() + str(summ))
                    other_part = None
                else:
                    result = BigInteger(result.toString() + str(summ)[1])
                    other_part = int(str(summ)[0])
                prob_self = prob_self.next
        elif len(self) < len(other):
            for i in range(len(self), len(other)):
                summ = int(prob_other.data)
                if other_part:
                    summ += other_part
                if summ < 10:
                    result = BigInteger(result.toString() + str(summ))
                    other_part = None
                else:
                    result = BigInteger(result.toString() + str(summ)[1])
                    other_part = int(str(summ)[0])
                prob_other = prob_other.next
        if other_part:   
            result = BigInteger(result.toString() + str(other_part))

        return BigInteger(result.toString()[::-1])

    def help_sub(self, other):
        """Help function for __sub__"""
        sub_one = False
        prob_self = self._int
        prob_other = other._int
        result = BigInteger()
        result._int.data = ''
        for i in range(len(other)):
            self_int = int(prob_self.data)
            other_int = int(prob_other.data)
            if sub_one:
                other_int += 1
            if self_int >= other_int:
                result._append_back(str(self_int - other_int))
                sub_one = False
            else:
                result._append_back(str(self_int + 10 - other_int))
                sub_one = True
            prob_self = prob_self.next
            prob_other = prob_other.next
        for i in range(len(other), len(self)):
            self_int = int(prob_self.data)
            if sub_one:
                if self_int == 0:
                    result._append_back('9')
                else:
                    result._append_back(str(self_int - 1))
                    sub_one = False
            else:
                result._append_back(prob_self.data)
            prob_self = prob_self.next
        if result._int.data == '0':
            result._int = result._int.next
        
        return BigInteger(result.toString()[::-1])

    def help_mul(self, digit):
        """Help function for __mul__"""
        help_self = BigInteger()
        for i in range(int(digit)):
            help_self += self
        return help_self

    def __add__(self, other):
        if self._last.data != '-' and other._last.data != '-':
            return self.help_add(other)
        elif self._last.data == '-' and other._last.data != '-':
            self_abs = self.sliced_minus()
            if self_abs > other:
                result = self_abs.help_sub(other)
                result._append_front('-')
                return result
            else:
                return other.help_sub(self_abs)
        elif self._last.data != '-' and other._last.data == '-':
            other_abs = other.sliced_minus()
            if other_abs > self:
                result = other_abs.help_sub(self)
                result._append_front('-')
                return result
            else:
                return self.help_sub(other_abs)
        elif self._last.data == '-' and other._last.data == '-':
            result = self.sliced_minus().help_add(other.sliced_minus())
            result._append_front('-')
            return result
        return BigInteger()

    def __sub__(self, other):
        if self == other:
            return BigInteger()
        other_minus = BigInteger(other.toString())
        if other_minus._last.data == '-':
            other_minus = other_minus.sliced_minus()
        else:
            other_minus._append_front('-')
        return self + other_minus

    def __mul__(self, other):
        minus = False
        self_abs = BigInteger(self.toString())
        other_abs = BigInteger(other.toString())
        if self._last.data == '-' or other._last.data == '-':
            minus = True
        if self._last.data == '-' and other._last.data == '-':
            minus = False
        result = BigInteger()
        other_abs = other_abs.sliced_minus()
        self_abs = self_abs.sliced_minus()
        prob_other = other_abs._int
        for i in range(len(other_abs)):
            next_sum = self_abs.help_mul(prob_other.data)
            prob_other = prob_other.next
            for j in range(i):
                next_sum._append_back('0')
            result += next_sum
        if minus:
            result._append_front('-')
        if result.toString() == '00' or result.toString() == '-00':
            return BigInteger()
        else:
            return result
    
    def __floordiv__(self, other):
        if other == BigInteger():
            raise ZeroDivisionError
        result = BigInteger()
        minus = False
        self_abs = BigInteger(self.toString())
        other_abs = BigInteger(other.toString())
        if self._last.data == '-' or other._last.data == '-':
            minus = True
        if self._last.data == '-' and other._last.data == '-':
            minus = False
        self_abs = self_abs.sliced_minus()
        other_abs = other_abs.sliced_minus()
        while self_abs >= other_abs:
            self_abs -= other_abs
            result += BigInteger('1')
        
        if minus and self_abs != BigInteger():
            result += BigInteger('1')
            result._append_front('-')
        elif minus:
            result._append_front('-')
        if result.toString() == '-0':
            return BigInteger()
        return result 

    def __mod__(self, other):
        if self == BigInteger():
            return BigInteger()
        if other == BigInteger():
            raise ZeroDivisionError
        result = self - (other * (self // other))
        return BigInteger(result.toString())

    def __pow__(self, other):
        result = BigInteger('1')
        minus = False
        self_abs = BigInteger(self.toString())
        other_abs = BigInteger(other.toString())
        if self._last.data == '-' and \
        other % BigInteger('2') == BigInteger('1'):
            minus = True
        self_abs = self_abs.sliced_minus()
        if other == BigInteger():
            return BigInteger('1')
        elif other > BigInteger():
            while other_abs > BigInteger():
                result *= self_abs
                other_abs -= BigInteger('1')
        else:
            raise Exception('Incorrect power')
        if minus:
            result._append_front('-')
        return result

    # binary
    def _to_bin(self):
        """Transfor integer to binary (without '0b')"""
        assert self >= BigInteger(), "Incorrect value"
        result = BigInteger()
        result._int.data = ''
        prob = self
        while prob > BigInteger('1'):
            result._append_front(str(prob % BigInteger('2')))
            prob = prob // BigInteger('2')
        result._append_front(str(prob % BigInteger('2')))
        return result
    
    def _to_int(self):
        """Transform binary to integer (without '0b')"""
        result = BigInteger()
        prob = self._int
        power = BigInteger()
        if self == BigInteger():
            return BigInteger()
        while prob.data == '0':
            prob = prob.next
        while prob:
            if prob.data == '1':
                result += BigInteger('2')**power
            power += BigInteger('1')
            prob = prob.next
        return result
    
    def __and__(self, other):
        assert self > BigInteger() and other > BigInteger(),\
            "Incorrect value"
        self_bin = self._to_bin()
        other_bin = other._to_bin()
        while len(other_bin) < len(self_bin):
            other_bin._append_front('0')
        result = BigInteger()
        result._int.data = ''
        prob_self = BigInteger(str(self_bin))._int
        prob_other = BigInteger(str(other_bin))._int
        while prob_self:
            res = int(prob_self.data) and int(prob_other.data)
            result._append_back(str(int(res)))
            prob_self = prob_self.next
            prob_other = prob_other.next
        while result._int.data != '1':
            result._int = result._int.next
        return BigInteger(str(result)[::-1])

    def __or__(self, other):
        assert self > BigInteger() and other > BigInteger(),\
            "Incorrect value"
        self_bin = self._to_bin()
        other_bin = other._to_bin()
        while len(other_bin) < len(self_bin):
            other_bin._append_front('0')
        result = BigInteger()
        result._int.data = ''
        prob_self = BigInteger(str(self_bin))._int
        prob_other = BigInteger(str(other_bin))._int
        while prob_self:
            res = int(prob_self.data) or int(prob_other.data)
            result._append_back(str(int(res)))
            prob_self = prob_self.next
            prob_other = prob_other.next
        while result._int.data != '1':
            result._int = result._int.next
        return BigInteger(str(result)[::-1])
    
    def __xor__(self, other):
        assert self > BigInteger() and other > BigInteger(),\
            "Incorrect value"
        self_bin = self._to_bin()
        other_bin = other._to_bin()
        while len(other_bin) < len(self_bin):
            other_bin._append_front('0')
        result = BigInteger()
        result._int.data = ''
        prob_self = BigInteger(str(self_bin))._int
        prob_other = BigInteger(str(other_bin))._int
        while prob_self:
            res = int(prob_self.data) ^ int(prob_other.data)
            result._append_back(str(int(res)))
            prob_self = prob_self.next
            prob_other = prob_other.next
        while result._int.data != '1':
            result._int = result._int.next
        return BigInteger(str(result)[::-1])

    def __lshift__(self, other):
        assert self > BigInteger() and other > BigInteger(),\
            "Incorrect value"
        result = self * BigInteger('2')**(other - BigInteger('1'))
        return result._to_bin()
    
    def __rshift__(self, other):
        assert self > BigInteger() and other > BigInteger(),\
            "Incorrect value"
        result = self // BigInteger('2')**(other + BigInteger('1'))
        return result._to_bin()
