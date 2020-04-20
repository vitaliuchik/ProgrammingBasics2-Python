class Polynomial:

    def __init__(self, coeffs):
        self.coeffs = list(coeffs)
        if len(self.coeffs) > 1:
            if self.coeffs[0] == 0:
                while self.coeffs[0] == 0:
                    if len(self.coeffs) == 1:
                        self.coeffs = []
                        break
                    else:
                        self.coeffs = self.coeffs[1:]
        elif len(self.coeffs) == 1 and self.coeffs[0] == 0:
            self.coeffs = []

    def __str__(self):
        return 'Polynomial(coeffs={})'.format(str(self.coeffs))

    def degree(self):
        return len(self.coeffs) - 1

    def coeff(self, deg):
        coeffs = self.coeffs[::-1]
        return coeffs[deg]

    def evalAt(self, x):
        result = 0
        coeffs = self.coeffs[::-1]
        for i in range(len(coeffs)):
            result += coeffs[i] * x**i
        return result

    def __eq__(self, other):
        if len(self.coeffs) == 1:
            return self.coeffs[0] == other
        return self.coeffs == other.coeffs

    def __ne__(self, other):
        if not isinstance(other, Polynomial):
            return True
        return self.coeffs != other.coeffs

    def __hash__(self):
        return hash(tuple(self.coeffs))

    def scaled(self, coeff):
        return Polynomial([i*coeff for i in self.coeffs])

    def derivative(self):
        coeffs = self.coeffs[::-1]
        der = [coeff*i for i, coeff in enumerate(coeffs)][1:]
        return Polynomial(der[::-1])

    def addPolynomial(self, other):
        if type(other) == Polynomial:
            coeffs = self.coeffs[::-1]
            other_coeffs = other.coeffs[::-1]
            min_len = min(len(coeffs), len(other_coeffs))
            new_c = [coeffs[i] + other_coeffs[i] for i in range(min_len)]
            if len(coeffs) > len(other_coeffs):
                new_c += coeffs[min_len:]
            elif len(other_coeffs) > len(coeffs):
                new_c += other_coeffs[min_len:]
            return Polynomial(new_c[::-1])

    def multiplyPolynomial(self, other):
        coeffs = self.coeffs[::-1]
        other_coeffs = other.coeffs[::-1]
        result = [0] * (len(coeffs) + len(other_coeffs) - 1)
        for o1,i1 in enumerate(coeffs):
            for o2,i2 in enumerate(other_coeffs):
                result[o1+o2] += i1*i2   
        return Polynomial(result[::-1])


class Quadratic(Polynomial):

    def __init__(self, coeffs):
        if len(coeffs) != 3:
            raise Exception
        super().__init__(coeffs)
        self.a = coeffs[0]
        self.b = coeffs[1]
        self.c = coeffs[2]

    def __str__(self):
        return 'Quadratic(a={}, b={}, c={})'.format(
            str(self.a), str(self.b), str(self.c))

    def discriminant(self):
        return self.b**2 - 4 * self.a * self.c

    def numberOfRealRoots(self):
        if self.discriminant() > 0:
            return 2
        elif self.discriminant() == 0:
            return 1
        else:
            return 0

    def getRealRoots(self):
        if self.discriminant() < 0:
            return []
        elif self.discriminant() == 0:
            return [-self.b / 2*self.a] 
        else:
            return [(-self.b - self.discriminant()**0.5)/ 2*self.a, \
                (-self.b + self.discriminant()**0.5)/ 2*self.a]