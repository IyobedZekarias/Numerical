# from Work.Real import sin, Real
from Work.Rational import Rational


def Trap(fn, n, a, b):
    e = Rational(1, 1e10)
    h = (b - a) / Rational(n, 1)
    s = Rational(1, 2) * (fn(a) + fn(b))
    for i in range(1, n):
        s = s + fn(a + Rational(i, 1) * h)
    return (h * s)


# f = Real(sin)
# a = Rational(0, 1)
# b = Rational(6, 1)
# n = 101
# print("integral 1: ", Trap(f, n, a, b))


# def func(e, x):
#     return f(e, x=x) / x

def Romb(a, b, fn, n):
    r = [[Rational(0, 1) for i in range(n)] for i in range(n)]
    h = b - a
    r[0][0] = Rational(1, 2) * h * (fn(a) + fn(b))

    po2 = 1
    for i in range(1, n):
        h = Rational(1, 2) * h

        sum = Rational(0, 1)
        po2 = 2 * po2
        for k in range(1, po2, 2):
            sum = sum + fn(a + k * h)

        r[i][0] = Rational(1, 2) * r[i-1][0] + sum * h

        po4 = 1
        for j in range(1, i + 1):
            po4 = 4 * po4
            r[i][j] = r[i][j-1] + (r[i][j-1] - r[i-1][j-1]) / (po4 - 1)
            # (Rational(po4, 1) - Rational(1, 1))

    return r[n-1][n-1]


# print("integral 2: ", r[n-1][n-1])