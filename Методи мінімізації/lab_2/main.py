import math

def f(x):
    return 1.5*pow((x+1.5), 2)*(x-1.1)*(x-0.75)


if __name__ == '__main__':
  # a = float(input('Input a: '))
  # b = float(input('Input b: '))
  # eps = float(input("Input eps: "))
  a = -1.55
  b = 2.4
  eps = 0.01
  L = b - a
  pres = 0.1
  print('[', a, b, ']', round(L, 3))


  while (L>pres):
    x1 = ((a + b)/2) - eps/2
    x2 = x1 + eps
    func_x1 = f(x1)
    func_x2 = f(x2)
    if func_x1 > func_x2:
      a = x1
    elif func_x1 < func_x2:
      b = x2
    else:
      a = x1
      b = x2
    L = b - a
    print(round(x1, 3), round(x2, 3), round(func_x1, 3), round(func_x2, 3), '[', round(a, 2), round(b, 2), ']', round(L, 3))

x = (a + b) / 2
print('x =', round(x, 3))