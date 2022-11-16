import math

def f(x):
    return 1.5*pow((x+1.5), 2)*(x-1.1)*(x-0.75)


if __name__ == '__main__':
  x0 = float(input('Input x0: '))
  delta = float(input("Input delta: "))

  k = 0
  p = 0

  check = 1;

  Xk = x0
  Xk_1 = Xk + delta

  func_0 = f(Xk)
  func_1 = f(Xk_1)
  print(k, delta, round(Xk,4), round(func_0,4))


  a, b = 0, 0

  while True:
    if func_1 < func_0:
      while func_1 < func_0:
        k += 1
        Xk = Xk_1
        Xk_1 = Xk + pow(2, k)*delta
        func_0 = func_1
        func_1 = f(Xk_1)
        print(k, abs(delta), round(Xk, 4), round(func_0, 4), bool(check))
        check = 1;
      a = Xk - delta
      b = Xk_1
      break
    else:
      check = 0
      if p == 0:
        delta = -delta
        p = 1
        Xk_1 = Xk + delta
        func_0 = f(Xk)
        func_1 = f(Xk_1)
      else:
        a = x0 + delta
        b = x0 - delta
        break

  print(round(a, 4), round(b, 4))