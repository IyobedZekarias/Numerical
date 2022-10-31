from Library.Rational import Rational


def f1(x):
    return (x**3 - (3 * x) + 1)


# @timeout(1)
def bis(a, b, e, fn):
    if type(a) != Rational:
        a = Rational(a, 1)
    if type(b) != Rational:
        b = Rational(b, 1)
    if type(e) != Rational:
        e = Rational(e, 1)
    xl = a
    xr = b
    while abs(xl - xr) >= e:
        c = (xl + xr)/2
        prod = fn(xl) * fn(c)
        if prod > e:
            xl = c
        else:
            if prod < e:
                xr = c
    return c


def f2(x):
    return (x**3 - (2 * x**2) + x - 3)


def df2(x):
    return ((3 * x**2) - (4 * x) + 1)


# @timeout(1)
def newt(e, fn, dfn, deltax):
    fxn = fn(deltax)
    count = 0
    while abs(fxn) >= e:
        Dfxn = dfn(deltax)
        deltax = deltax - (fxn / Dfxn)
        fxn = fn(deltax)
        count += 1
        if(count > 60):
            return -1
    return deltax


def f3(x):
    # return (x**5 + x**3 + 3)
    return ((2 * x**2) - 10)


def sec(n, fn):
    a = Rational(-1, 1)
    b = Rational(1, 1)
    fa = fn(a)
    fb = fn(b)
    if abs(fa) > abs(fb):
        a, b = b, a
        fa, fb = fb, fa

    for i in range(2, n):
        if abs(fa) > abs(fb):
            a, b = b, a
            fa, fb = fb, fa
        d = (b - a)/(fb - fa)
        b = a
        fb = fa
        d = d * fa
        # if abs(d) < e:
        #     print("here")
        #     return d
        a = a - d
        fa = fn(a)
    return b


# print(bis(0, 1, Rational(1, 1e30)))
# print(newt(Rational(1, 1e2), f2, df2, Rational(3, 1)))
# print(sec(8, f3))
