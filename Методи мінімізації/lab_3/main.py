import math

def toFixed(num, digits = 3):
    return f"{num:6.{digits}f}".format(12)

def f(x):
    return 1.5*pow((x+1.5), 2)*(x-1.1)*(x-0.75)

def calc(a, b, eps):
    L = b - a
    while L > eps:
        x1 = a + 0.25 * L
        x2 = b - 0.25 * L
        xm = (a + b) / 2
        print(toFixed(x1), toFixed(xm), toFixed(x2), toFixed(f(x1)), toFixed(f(xm)), toFixed(f(x2)), '[' , toFixed(a), toFixed(b), ']' ,toFixed(L))
        if (f(x1) < f(xm)):
            b = xm
            xm = x1
        else:
            if (f(x2) < f(xm)):
                a = xm
                xm = x2
            else:
                a = x1
                b = x2
        L = b - a
    print(xm)
    return xm, f(xm), L

if __name__ == '__main__':
    x, y, L = calc(-1.55, 2, 0.01)