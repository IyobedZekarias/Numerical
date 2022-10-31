from numpy import ones
from Library.Rational import Rational
from Library.Real import Real, sin, cos


def f1(x):
    return (Rational(1, 1) / (Rational(1, 1) + x**2))


def f2(x):
    error = Rational(1, 10**10)
    sf = Real(sin)
    return (sf(error, x=x) / x**2)


def f3(x):
    error = Rational(1, 10**10)
    sc = Real(cos)
    return (sc(error, x=x) / x)


def Simpson(f, a, b, tol, level, level_max):
    level += 1
    h = (b - a)
    c = (a + b) / Rational(2, 1)
    oneSimpson = (h * (f(a) + (Rational(4, 1) * f(c)) + f(b))) / Rational(6, 1)
    d = (a + c) / Rational(2, 1)
    e = (c + b) / Rational(2, 1)
    twoSimpson = (h * (f(a) + (Rational(4, 1) * f(d)) + (Rational(2, 1)
                                                         * f(c)) + (Rational(4, 1) * f(e)) + f(b))) / Rational(12, 1)

    if level >= level_max:
        return twoSimpson
    else:
        if (abs(twoSimpson - oneSimpson) < tol):
            return twoSimpson + ((twoSimpson - oneSimpson) / Rational(15, 1))
        else:
            lSimp = Simpson(f, a, c, tol/Rational(2, 1), level, level_max)
            rSimp = Simpson(f, c, b, tol/Rational(2, 1), level, level_max)
            return lSimp + rSimp


# eps = Rational(.5, 10**5)
# ans1 = Simpson(f1, Rational(0, 1), Rational(1, 1), eps, 0, 4)
# ans1 *= 4
# print('\neq 1:        ', ans1)
# print('eq 1 approx: ', ans1.numerator()/ans1.denominator(), '\n')

# ans2 = Simpson(f2, Rational(13, 10), Rational(
#     219, 100), eps, 0, 4)
# print('eq 2:        ', ans2)
# print('eq 2 approx: ', ans2.numerator()/ans2.denominator(), '\n')

# ans3 = Simpson(f3, Rational(13, 10), Rational(
#     219, 100), eps, 0, 4)
# print('eq 3:        ', ans3)
# print('eq 3 approx: ', ans3.numerator()/ans3.denominator(), '\n')
