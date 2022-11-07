from Zeros import newt, bis
from Work.Rational import Rational, TimeoutError
from tqdm import tqdm


def p1(*args, **kwargs):
    bounds = kwargs.get('b', [])
    bounds.append(-15 / 2)
    bounds.append(15 / 2)
    if len(args) > 0:
        x = args[0]
        return ((2 * (x**7)) - (10 * (x**5)) - (2 * (x**4)) + (x**2) + (15 * x) + 5)


def dp1(x):
    return ((14 * (x**6)) - (50 * (x**4)) - (8 * (x**3)) + (2 * x) + 15)


def p2(*args, **kwargs):
    bounds = kwargs.get('b', [])
    bounds.append(-3600 / .22)
    bounds.append(3600 / .22)
    if len(args) > 0:
        x = args[0]
        return ((.22 * (x**5)) - (25 * (x**4)) - (3600 * (x**3)) + (.1 * (x**2)) - 367)


def dp2(x):
    return ((x * ((11 * (x**3)) - (1000 * (x**2)) - (108000 * x) + 2)) / 10)


def p3(*args, **kwargs):
    bounds = kwargs.get('b', [])
    bounds.append(-2 / 2)
    bounds.append(2 / 2)
    if len(args) > 0:
        x = args[0]
        return ((2 * (x**8)) - (2 * (x**4)) + .5)


def dp3(x):
    return ((16 * (x**7)) - (8 * (x**3)))


def zero(f1, df1, **kwargs):
    bound = []
    f1(b=bound)
    lbound = kwargs.get('lo', bound[0])
    rbound = kwargs.get('hi', bound[1])
    f1zeros = []
    checkcount = 0
    j = lbound
    pbar = tqdm(total=rbound-lbound, leave=False)
    while j < rbound + 1:
        # Loop through possible errors 10^i because some can cause overflow, timeout, or to many iterations.
        # This way there will likely be a good error found between 10^-5 and 10^-3 it breaks after it has
        #   Found one and continues the upper loop
        for i in range(-5, -3):
            try:
                x = newt(Rational(10**i, 1), f1, df1, Rational(j, 1))
                # Newtons returns -1 for to many iterations
                if x == -1:
                    break
                # print(x.numerator()/x.denominator(), "   ", 10**i)
                z = x.numerator()/x.denominator()
                if z <= lbound:
                    continue
                zr = z + .0005
                zl = z - .0005
                # Bisection is implemented using value that netwons returns +- .0005
                e = kwargs.get('e', Rational(1, 1e11))
                z = bis(zl, zr, e, f1)
                # Only append to the array if value has not already been inserted using 'check' as flag
                check = True
                for k in f1zeros:
                    kval, zval = k.numerator()/k.denominator(), z.numerator()/z.denominator()
                    kstr, zstr = str(kval), str(zval)
                    kdig, zdig = kstr.index('.'), zstr.index('.')
                    if round(kval, 4-len(kstr[0:kdig])) == round(zval, 4-len(zstr[0:zdig])):
                        check = False
                        checkcount += 1
                        break
                if check:
                    f1zeros.append(z)
                    # Most times will be jumping forward becuase zero will be discovered from left side most times
                    j = z.numerator()/z.denominator()
                    checkcount = 0
                # Make performance jumps if keep discovering the same root by doubling j
                if checkcount == 30:
                    j += abs(j)
                    if j > 0:
                        pbar.update(n=abs(j)*2)
                    checkcount -= 10
                break
            except (TimeoutError, OverflowError) as e:
                continue
        j += .5
        pbar.update(n=.5)
    pbar.close()
    return f1zeros


# This gets the bounds
bound = []
p1(b=bound)
print("FOR PROBLEM 1 \n  ƒ(x) = 0  ",
      bound[0], " <= x <= ", bound[1], " \n  FOR THE FOLLOWING\n------------------------------- ")
# lo and hi are set manually here and could also be set to specific values to only get
# positive  zeros for example
prob = zero(p1, dp1, lo=bound[0], hi=bound[1])
for i in prob:
    print("     ", i, " = ".ljust(4), round(i.numerator()/i.denominator(), 11))

print("\n")
bound.clear()
p2(b=bound)
print("FOR PROBLEM 2 \n  ƒ(x) = 0  ",
      round(bound[0], 1), " <= x <= ", round(bound[1], 1), " \n  FOR THE FOLLOWING\n------------------------------- ")
prob = zero(p2, dp2)

for i in prob:
    print("     ", i, " = ".ljust(4), round(i.numerator()/i.denominator(), 11))

print("\n")
bound.clear()
p3(b=bound)
print("FOR PROBLEM 1 \n  ƒ(x) = 0  ",
      bound[0], " <= x <= ", bound[1], " \n  FOR THE FOLLOWING\n------------------------------- ")
prob = zero(p3, dp3)
for i in prob:
    print("     ", i, " = ".ljust(4), round(i.numerator()/i.denominator(), 11))
