from Library.Rational import Rational
from inspect import signature


class Real(object):
    def __init__(self, fn):
        self._fn = fn

    def __call__(self, e, **kwargs):
        sig = signature(self._fn)
        params = sig.parameters
        if(len(params) == 1):
            return self._fn(e)
        elif(len(params) == 2):
            return self._fn(e, kwargs.get("x", None))

    def __add__(self, other):
        def ret(n): return self._fn(
            n/Rational(2, 1) + other._fn(n/Rational(2, 1)))
        return Real(ret)

    def __sub__(self, other):
        def ret(n): return self._fn(
            n/Rational(2, 1) - other._fn(n/Rational(2, 1)))
        return Real(ret)

    def __mul__(self, other):
        def ret(n): return self._fn(
            n**Rational(2, 1) * other._fn(n**Rational(2, 1)))
        return Real(ret)

    def __truediv__(self, other):
        def ret(n): return self._fn(
            n**Rational(2, 1) / other._fn(n**Rational(2, 1)))
        return Real(ret)

    def __pow__(self, a):
        def ret(n): return self._fn(n**Rational(2, 1))
        return Real(ret**a)


def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact


def sinerr(e, x):
    n = 0
    while(Rational((x.numerator()/x.denominator())**(2*n + 1), factorial(2 * n + 1)) > e):
        n += 1
    return n


def sin(e, x):
    n = sinerr(e, x)
    res = Rational((x.numerator()/x.denominator())
                   ** (2*0 + 1), factorial(2 * 0 + 1))
    for k in range(1, n):
        res += Rational(
            ((-1)**k) * ((x.numerator()/x.denominator())**(2*k + 1)),
            factorial(2 * k + 1))
    return res


def coserr(e, x):
    n = 0
    while(Rational((x.numerator()/x.denominator())**(2*n), factorial(2 * n)) > e):
        n += 1
    return n


def cos(e, x):
    n = coserr(e, x)
    res = Rational(1, 1)
    for k in range(1, n):
        res += Rational(
            (((-1)**k) * ((x.numerator()/x.denominator())**(2*k))),
            factorial(2 * k)
        )
    return res

# use absolute vlaue of the term not the actual term


def eerr(e, x):
    n = 0
    while(Rational((x.numerator()/x.denominator())**n, factorial(n)) > e):
        n += 1
    return n


def em(e, x):
    n = eerr(e, x)
    res = Rational(1, 1)
    for k in range(1, n):
        res = res + Rational((-(x.numerator()/x.denominator()))**k, factorial(k))

    return (Rational(1, 1) / res)


def esqrt(e, x):
    n = 0
    while(Rational(((x.numerator()//x.denominator())**(.5-n) * (-(x.numerator()//x.denominator()) + (x.numerator()//x.denominator()))**n), 1) > e):
        n += 1
    return n


def sqrt(e, x):
    if(x <= Rational(1, 1e10)):
        return Rational(0, 0)

    n = esqrt(e, x)
    res = Rational(((x.numerator()//x.denominator())**(.5-0) *
                    (-(x.numerator()//x.denominator()) + (x.numerator()//x.denominator()))**0), 1)
    for k in range(2, n):
        res += Rational(((x.numerator()//x.denominator())**(.5-k) *
                        (-(x.numerator()//x.denominator()) + (x.numerator()//x.denominator()))**k), 1)
    return res


def earctan(e, x):
    n = 0
    while (Rational(((1)**n) * (x.numerator()/x.denominator())**(2 * n + 1), 2 * n + 1) > e):
        n += 1
    return n


def arctan(e, x):
    n = earctan(e, x)
    res = x
    for k in range(1, n):
        res += Rational(((-1)**k) * (x.numerator()/x.denominator())**(2 * k + 1),
                        2 * k + 1)
    return res



def enatlog(e, x):
    n = 1
    while( abs(Rational(-1, 1)**(n-1) * Rational((x.numerator()/x.denominator())**(n), n)) > e):
        n += 1
    return n

def natlog(e, x): 
    n = enatlog(e, x)
    res = x
    # print(n)
    for k in range(2, n): 
        res += ((-1)**(k-1) *
                Rational((x.numerator()/x.denominator())**(k), k))
    return res

# π / 4 = 4 * arctan(1/5) - arctan(1/239)


def pi(e):
    onefift = Real(arctan)
    one239 = Real(arctan)
    onefift = onefift(e, x=Rational(1, 5))
    one239 = one239(e, x=Rational(1, 239))
    return Rational(4, 1) * (Rational(4, 1) * onefift - one239)


# ln = Real(natlog)
# print(ln(Rational(1, 1e10), x=Rational(5, 7)))

# sinR = Real(sin)
# print("Sin(3): ", sinR(Rational(1, 1e10), x=Rational(100, 1)))

# eer = Real(em1)
# print("e^1: ", eer(Rational(1, 1e10)))

# sqrt2 = Real(sqrt)
# print("√2: ", sqrt2(Rational(1, 1e10), x=Rational(2, 1)))

# r1 = sinR(Rational(1, 1e10), x=Rational(3, 1)) + \
#     sqrt2(Rational(1, 1e10), x=Rational(2, 1))
# print(r1)

# sqrt3 = Real(sqrt)
# print("√3: ", sqrt3(Rational(1, 1e10), x=Rational(3, 1)))

# arctanR = Real(pi)
# print("π: ", pi(Rational(1, 1e21)))
