from cmath import log
from math import exp
from operator import mod
import matplotlib.pyplot as plt
import numpy as np

def PsRandom(x, seed, a, b, **kwargs):
    type = kwargs.get("type", float)
    k, j = 16807, 2**63 - 1
    for i in range(len(x)): 
        seed = mod(k * seed, j)
        x[i] = type((b - a) * seed/j + a)
    return seed;
    

# x = [0] * 1000
# PsRandom(x, 2**32, 1, 100, type=int)

# frequency, bins = np.histogram(x, bins=100, range=[0, 100])
# plt.hist(x, bins=99)
# plt.gca().set(title='Frequency Histogram', ylabel='Frequency')
# # plt.show()

# def fn1(x):
#     return (4 - x**2)**.5

# def fn2(x, y, z):
#     return (x**2 + y**2 + z**2)

# def fn3(x, y, z):
#     return ((y*x**2) + z * log(y) + exp(x))


# # --- FIRST INTEGRAL
# u = [0] * 2500
# PsRandom(u, 2**32, 0, 2, type=float)
# a = 0
# b = 2
# ret = 0
# for i in u:
#     ret += fn1(i)
# ret *= ((b-a)/len(u))

# print("pi = ", ret)

# x = [0] * 2500
# y = [0] * 2500
# z = [0] * 2500

# seed = PsRandom(x, 2**32, -1, 1, type=float)
# seed = PsRandom(y, seed, -1, 1, type=float)
# PsRandom(z, seed, -1, 1, type=float)


# # --- SECOND INTEGRAL
# a = -1
# b = 1
# ret = 0
# for i in range(len(x)):
#     ret += fn2(x[i], y[i], z[i])

# ret *= ((b-a)**3/len(x))
# print("second integral: ", ret)


# # --- THRID INTEGRAL
# xa = -1
# xb = 1
# ya = 3
# yb = 6
# za = 0
# zb = 2
# seed = PsRandom(x, 2**32, xa, xb, type=float)
# seed = PsRandom(y, seed, ya, yb, type=float)
# PsRandom(z, seed, za, zb, type=float)

# ret = 0
# for i in range(len(x)):
#     ret += fn3(x[i], y[i], z[i])

# ret *= (xb - xa) * (yb - ya) * (zb - za)/len(x)
# print("third integral: ", ret.real)

