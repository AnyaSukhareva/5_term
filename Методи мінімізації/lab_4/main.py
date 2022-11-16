#Function
f = lambda x: 1.5*pow((x+1.5), 2)*(x-1.1)*(x-0.75)

#Initial guess
a = -1.55; b = 2

print (' x      x1          x2     f(x1)    f(x2)     [ a    ,    b ]        L')
i = 1
R = (5 ** 0.5 - 1) / 2
L  = b - a
x2 = a + R*L
x1 = a + b - x2
f1 = f(x1)
f2 = f(x2)
eps = 0.1

print(f"{0:>2}   {'':>8.5}   {'':>8.5} {'':>8.5} {'':>8.5} {'['}{a:>8.5f} {b:>8.5f} {']'} {L:>8.5f}")

#Golden-Section Search Method
while L > eps:
    if f1 < f2:
        b = x2
        x2 = x1
        f2 = f1
        x1 = a + b - x2
        f1 = f(x1)
    else:
        a = x1
        x1 = x2
        f1 = f2
        x2 = a + b - x1
        f2 = f(x2)
    L = b - a
    print(f"{i:>2}   {x1:>8.5f}   {x2:>8.5f} {f1:>8.5f} {f2:>8.5f} {'['}{a:>8.5f} {b:>8.5f} {']'} {L:>8.5f}")
    i += 1

x=(a+b)/2
print('Result:', x)
