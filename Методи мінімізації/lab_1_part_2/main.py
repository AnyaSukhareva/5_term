import math
import numpy as np
from prettytable import PrettyTable

class Vector(object):
    def __init__(self, x, y):
        """ Create a vector, example: v = Vector(1,2) """
        self.x = x
        self.y = y

    def __repr__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __rmul__(self, other):
        x = self.x * other
        y = self.y * other
        return Vector(x, y)

    def __truediv__(self, other):
        x = self.x / other
        y = self.y / other
        return Vector(x, y)

    def c(self):
        return (self.x, self.y)


# objective function
def f(point):
   x1, x2 = point
   return ((1-x1)**2) + ((2 - x2)**2) - x1 - x2
   #return x1**2 + x2**2

def nelder_mead(coord1, coord2, alfa, lamb, beta, gamma):
    prettyTable = PrettyTable()
    iter = 0
    prettyTable.field_names = ["№", "Best", "f(Best)", "Good", "f(Good)", "Worst", "f(Worst)", "eps"]

    # initialization
    N = 2
    v1 = Vector(coord1, coord2)
    sigma1 = ((math.sqrt(N+1) + N - 1)/(N*math.sqrt(2)))*alfa
    sigma2 = ((math.sqrt(N+1) - 1)/(N*math.sqrt(2)))*alfa
    v2 = Vector(coord1 + sigma2, coord2 + sigma1)
    v3 = Vector(coord1 + sigma1, coord2 + sigma2)
    D = 1

    while(D**(1/2) >= 0.001):
        adict = {v1: f(v1.c()), v2: f(v2.c()), v3: f(v3.c())}
        points = sorted(adict.items(), key=lambda x: x[1])

        b = points[0][0]
        g = points[1][0]
        w = points[2][0]

        mid = (g + b) / 2
        xr = mid + lamb * (mid - w)
        f_xr = f(xr.c())
        f_g = f(g.c())
        f_w = f(w.c())
        f_b = f(b.c())

        # reflection
        xr = mid + lamb * (mid - w)
        if f_xr < f_g:
            w = xr
        else:
            if f_xr < f_w:
                w = xr
            c = (w + mid) / 2
            f_c = f(c.c())
            if f_c < f_w:
                w = c

        if f_xr < f_b:
            # expansion
            xe = mid + gamma * (xr - mid)
            f_xe = f(xe.c())
            if f_xe < f_xr:
                w = xe
            else:
                w = xr

        if f_xr > f_g:
            # contraction
            xc = mid + beta * (w - mid)
            f_xc = f(xc.c())
            if f_xc < f_w:
                w = xc

        # update points
        v1 = w
        v2 = g
        v3 = b
        f_v1 = f(v1.c())
        f_v2 = f(v2.c())
        f_v3 = f(v3.c())
        D = np.var([f_v1, f_v2, f_v3])
        iter += 1
        prettyTable.add_row([iter, v3, f_v3, v2, f_v2, v1, f_v1, D])
    print(prettyTable)
    return b, f_b


print("Result of Nelder-Mead algorithm: ")
xk, f = nelder_mead(-1, 6, 2, 1, 0.5, 2)
print("Best poits is: %s" % (xk))
print("Result is: %s" % (f))