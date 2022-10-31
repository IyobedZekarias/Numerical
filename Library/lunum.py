from Library.Rational import Rational
from Library.Real import em, cos as cs, sin as sn, Real
from Library.Gaussian import dumb as nv, better as gs
from Library.Zeros import bis as zbis, sec as zsec
from Library.InterpExterp import NDD, poly, Ext
from Library.integral import Trap as itrp, Romb as irmb
from Library.Simpson import Simpson as ssmp01
from Library.Spline import SplineEval as spe
from Library.MonteCarlo import PsRandom as psr
from cmath import log
from math import exp
import copy

def x1(x): 
    return (Rational(1, 1) / x)

eps = Rational(1, 1e20)

def ln(x):
    Rat = 1
    if type(x) == float or type(x) == int: 
        Rat = 0
        x = Rational(x, 1)
    ans = ssmp01(x1, Rational(1, 1), x, eps, 0, 6)
    if not Rat: 
        ans = ans.numerator()/ans.denominator()
    return ans


def e(x): 
    Rat = 1
    if type(x) == float or type(x) == int:
        Rat = 0
        x = Rational(x, 1)
    func = Real(em)
    ans = func(eps, x=x)
    if not Rat:
        ans = ans.numerator()/ans.denominator()
    return ans

def cos(x):
    Rat = 1
    if type(x) == float or type(x) == int:
        Rat = 0
        x = Rational(x, 1)
    func = Real(cs)
    ans = func(eps, x=x)
    if not Rat:
        ans = ans.numerator()/ans.denominator()
    return ans

def sin(x): 
    Rat = 1
    if type(x) == float or type(x) == int:
        Rat = 0
        x = Rational(x, 1)
    func = Real(sn)
    ans = func(eps, x=x)
    if not Rat:
        ans = ans.numerator()/ans.denominator()
    return ans

def NaiveGauss(x):
    ogx = copy.deepcopy(x)
    Rat = 1
    if type(x[0][0]) == float or type(x[0][0]) == int:
        Rat = 0
        for i in range(len(x)): 
            for j in range(len(x[0])): 
                ogx[i][j] = Rational(ogx[i][j], 1)
    ans = nv(ogx)
    if not Rat:
        for i in range(len(ans)):
            ans[i] = ans[i].numerator()/ans[i].denominator()
    return ans


def Gauss(x):
    ogx = copy.deepcopy(x)
    Rat = 1
    if type(x[0][0]) == float or type(x[0][0]) == int:
        Rat = 0
        for i in range(len(x)):
            for j in range(len(x[0])):
                ogx[i][j] = Rational(x[i][j], 1)
    ans = gs(ogx)
    if not Rat:
        for i in range(len(ans)):
            ans[i] = ans[i].numerator()/ans[i].denominator()
    return ans


def bisection(function, lowerbound, upperbound):
    Rat = 1
    if type(lowerbound) == float or type(lowerbound) == int:
        Rat = 0
    ans = zbis(lowerbound, upperbound, eps, function)
    if not Rat:
        ans = ans.numerator()/ans.denominator()
    return ans


def secant(function, **kwargs):
    type = kwargs.get('type', Rational)
    depth = kwargs.get('depth', 8)
    ans = zsec(depth, function)
    if type != Rational: 
        return type(ans.numerator()/ans.denominator())
    return ans

def NewtonInterp(x, xpoints, ypoints): 
    xpointsc = copy.deepcopy(xpoints)
    ypointsc = copy.deepcopy(ypoints)
    Rat = 1
    if type(x) == float or type(x) == int: 
        Rat = 0
        for i in range(len(xpointsc)): 
            xpointsc[i] = Rational(xpointsc[i], 1)
            ypointsc[i] = Rational(ypointsc[i], 1)
        x = Rational(x, 1)
    n = NDD(xpointsc, ypointsc)
    ans = poly(x, xpointsc, n)
    if not Rat: 
        ans = ans.numerator()/ans.denominator()
    return ans


def RichExtrap(function, x, **kwargs):
    lowerbound = kwargs.get('l', 0)
    upperbound = kwargs.get('u', 9)
    Rat = 1
    if type(x) == float or type(x) == int: 
        x = Rational(x, 1)
        Rat = 0
    ans = Ext(function, x, lowerbound, upperbound)
    if not Rat: 
        for i in range(len(ans)): 
            for j in range(len(ans[0])): 
                ans[i][j] = ans[i][j].numerator()/ans[i][j].denominator()
    return ans

def Trapezoidal(function, a, b, **kwargs):
    depth = kwargs.get("n", 200)
    Rat = 1
    if type(a) == float or type(b) == int: a, Rat = Rational(a, 1), 0
    if type(b) == float or type(b) == int: b, Rat = Rational(b, 1), 0
    ans = itrp(function, depth, a, b)
    if not Rat: 
        return ans.numerator()/ans.denominator()
    else: 
        return ans

def Romberg(function, a, b, **kwargs): 
    depth = kwargs.get("n", 8)
    Rat = 1
    if type(a) == float or type(b) == int: a, Rat = Rational(a, 1), 0
    if type(b) == float or type(b) == int: b, Rat = Rational(b, 1), 0
    ans = irmb(a, b, function, depth)
    if not Rat: 
        return ans.numerator()/ans.denominator()
    else:
        return ans

def Simpson(function, a, b, **kwargs):
    level = kwargs.get("level", 0)
    level_max = kwargs.get("mlevel", 4)
    Rat = 1
    if type(a) == float or type(b) == int: a, Rat = Rational(a, 1), 0
    if type(b) == float or type(b) == int: b, Rat = Rational(b, 1), 0
    ans = ssmp01(function, a, b, Rational(1, 1e10), level, level_max)
    if not Rat: 
        return ans.numerator()/ans.denominator()
    else:
        return ans

def Spline(x, xpoints, ypoints): 
    xpointsc = copy.deepcopy(xpoints)
    ypointsc = copy.deepcopy(ypoints)
    Rat = 1
    zpoints = [Rational(0, 1) for i in range(len(xpointsc))]
    if type(xpointsc[0]) == float or type(xpointsc[0]) == int:
        Rat = 0
        for i in range(len(xpointsc)):
            xpointsc[i] = Rational(xpointsc[i], 1)
            ypointsc[i] = Rational(ypointsc[i], 1)
        x = Rational(x, 1)
    ans = spe(xpointsc, ypointsc, zpoints, x)
    if not Rat:
        ans = ans.numerator()/ans.denominator()
    return ans

def Rand(list, lower_range, upper_range, **kwargs): 
    seed = kwargs.get("seed", 2**32)
    typ = kwargs.get("type", float)
    return psr(list, seed, lower_range, upper_range, type=typ)

def MonteCarlo(function, *args, **kwargs):
    size = kwargs.get("rep", 2500)
    args = args[::-1]
    if len(args) == 0: return
    lists = [[0 for i in range(size)] for j in range(len(args))]
    seed = 2**32
    rangetot = 1
    for i in range(len(args)): 
        seed = Rand(lists[i], args[i][0], args[i][1], seed=seed)
        rangetot *= (args[i][1] - args[i][0])
    rangetot /= len(lists[0])
    ret = 0
    for i in range(len(lists[0])): 
        u = [0] * len(lists)
        for j in range(len(lists)): 
            u[j] = lists[j][i]
        ret += function(u)
    ret *= rangetot
    if type(ret) == complex: return ret.real
    return ret





# -------------------- EXAMPLES FROM HERE ---------------------------- #
def f3(x):
    return (x**5 + x**3 + 3)


def mofun(args):
    return ((args[1]*args[0]**2) + args[2] * log(args[1]) + exp(args[0]))


# mat = [[2, 4, -2, -2, -4],
#        [1, 2, 4, -3, 5],
#        [-3, -3, 8, -2, 7],
#        [-1, 1, 6, -3, 7]]

# val = Gauss(mat)

# print(val)

# ans = secant(f3, Rational)
# print(ans)


# D = Simpson(f3, 0, 10, mlevel=10)
# print(D)
# D = Trapezoidal(f3, 0, 10, n=1000)
# print(D)

# x = []
# y = [Rational(1 ,    1), Rational(941, 1000), Rational(8   ,   10),
#     Rational(64 ,  100), Rational(5  ,   10), Rational(39  ,  100),
#     Rational(307, 1000), Rational(246, 1000), Rational(2   ,   10),
#     Rational(164, 1000), Rational(137, 1000), Rational(116 , 1000),
#     Rational(1  ,   10), Rational(86 , 1000), Rational(75  , 1000),
#     Rational(66 , 1000), Rational(58 , 1000), Rational(52  , 1000),
#     Rational(47 , 1000), Rational(42 , 1000)]

# for i in range(20):
#     x.append(Rational(i, 4))

# D = Spline(Rational(125, 1000), x, y)
# print(D)

# D = MonteCarlo(mofun, 2500, (-1, 1), (3, 6), (0, 2))
# print(D)