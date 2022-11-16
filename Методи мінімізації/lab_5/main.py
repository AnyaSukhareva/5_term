#Function
f = lambda x: 1.5*pow((x+1.5), 2)*(x-1.1)*(x-0.75)
#Initial guess
a = -1.55; b = 2

print (' x      x1          x2     f(x1)    f(x2)     [ a    ,    b ]        L')
i = 1
L  = b - a
eps = 0.1
num = L / eps

fib1 = 1
fib2 = 1
i = 0
while num >= fib2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1

k=i
R = fib1/fib2
n = 1
x2 = a + R*L
x1 = a + b - x2
f1 = f(x1)
f2 = f(x2)

print(f"{0:>2}   {'':>8.5}   {'':>8.5} {'':>8.5} {'':>8.5} {'['}{a:>8.5f} {b:>8.5f} {']'} {L:>8.5f}")
#Fibonacci Search Method
while k >= n:
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
    print(f"{n:>2}   {x1:>8.5f}   {x2:>8.5f} {f1:>8.5f} {f2:>8.5f} {'['}{a:>8.5f} {b:>8.5f} {']'} {L:>8.5f}")
    n += 1

x=(a+b)/2
print('Result:', x)