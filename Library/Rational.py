class Rational(object):
    def __init__(self, num, denom):

        if denom != 0:
            self._num = num
            self._denom = denom
            self.__reduce()
        else:
            self._num = 0
            self._denom = 0

    # return numerator
    def numerator(self):
        return self._num

    # return denominator
    def denominator(self):
        return self._denom

    # return string of number
    def __str__(self):
        return str(int(self._num)) + "/" + str(int(self._denom))

    def __gcd(self, a, b):
        (a, b) = (max(abs(a), abs(b)), min(abs(a), abs(b)))
        while b > 0:
            (a, b) = (b, a % b)
        return a

    # # reduce numerator and denominator by the gcd
    def __reduce(self):
        gcd = self.__gcd(self._num, self._denom)
        self._num //= gcd
        self._denom //= gcd

    # overload the + operator
    def __add__(self, other):
        if type(other) != Rational:
            other = Rational(other, 1)
        return Rational((self._num * other._denom + other._num * self._denom), (self._denom * other._denom))

    # overload the - operator
    def __sub__(self, other):
        if type(other) != Rational:
            other = Rational(other, 1)
        return Rational((self._num * other._denom - other._num * self._denom), (self._denom * other._denom))

    # overload the * operator
    def __mul__(self, other):
        if type(other) == Rational:
            return Rational((self._num * other._num), (self._denom * other._denom))
        else:
            return Rational((self._num * other), self._denom)

    def __rmul__(self, a):
        return Rational((self._num * a), (self._denom))

    # overload the / operator
    def __truediv__(self, other):
        if type(other) != Rational:
            other = Rational(other, 1)
        return Rational((self._num * other._denom), (self._denom * other._num))

    # overload the ** operator
    def __pow__(self, a):
        return Rational((self._num ** a), (self._denom ** a))

    # over load the < operator
    def __lt__(self, other):
        extremes = self._num * other._denom
        means = other._num * self._denom
        return extremes < means

    # overload the == operator
    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self._num == other._num and self._denom == other._denom

    # overload the <= operator
    def __le__(self, other):
        return not(self > other)

    # overload the >= operator
    def __ge__(self, other):
        return not(self < other)

    # overload the > operator
    def __gt__(self, other):
        extremes = self._num * other._denom
        means = other._num * self._denom
        return extremes > means

    # overload the != operator
    def __neq__(self, other):
        return not(self == other)

    # overload the abs() ope
    def __abs__(self):
        return Rational(abs(self._num), abs(self._denom))
