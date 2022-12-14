import math
from prettytable import PrettyTable


def func(x):
    # return x**2
    return 1.5*pow((x+1.5), 2)*(x-1.1)*(x-0.75)


def get_min_index(arr):
    m_min = arr[0]
    index = 0
    for i in range(1, len(arr)):
        if arr[i] < m_min:
            m_min = arr[i]
            index = i
    return index


def get_max_index(arr):
    m_max = arr[0]
    index = 0
    for i in range(1, len(arr)):
        if arr[i] > m_max:
            m_max = arr[i]
            index = i
    return index


def calc(x1, dx, Sx, Sf):
    prettyTable = PrettyTable()
    prettyTable.field_names = ["x1", "x2", "x3", "f(x1)", "f(x2)", "f(x3)", "qx", "f(qx)"]

    f = [0, 0, 0]  # f1, f2, f3
    x = [x1, 0, 0]  # x1, x2, x3

    # step 2
    x[1] = x[0] + dx
    f[0] = func(x[0])
    f[1] = func(x[1])

    # step 3
    if f[0] > f[1]:
        x[2] = x[0] + 2 * dx
    else:
        x[2] = x[0] - dx
    f[2] = func(x[2])

    while True:
        # step 4
        index_min = get_min_index(f)
        index_max = get_max_index(f)
        f_min = f[index_min]
        x_min = x[index_min]

        # step 5
        a1 = (f[1] - f[0]) / (x[1] - x[0])
        a2 = 1 / (x[2] - x[1]) * ((f[2] - f[0]) / (x[2] - x[0]) - a1)

        # step 6
        qx = -a1 / (2 * a2) + (x[0] + x[1]) / 2
        f_qx = func(qx)

        prettyTable.add_row([x[0], x[1], x[2], f[0], f[1], f[2], qx, f_qx])

        # step 7
        if abs(f_min - f_qx) <= Sf and abs(x_min - qx) <= Sx:
            print(prettyTable)
            return qx
        else:
            x[index_max] = qx
            f[index_max] = f_qx


if __name__ == '__main__':
    x1, dx, Sx, Sf = -1.55, 0.1, 0.01, 0.001
    result = calc(x1, dx, Sx, Sf)
    print(result)