import sys
import math


def main():
    n = int((lambda: sys.stdin.readline())())

    data_set = []

    for i in range(0, n):
        data_set.append(map(int, (lambda: sys.stdin.readline())().split()))

    for i in range(0, n):
        a = data_set[i][0]
        b = data_set[i][1]

        print getRemain(a, b)


def getRemain(base, exp):

    remain = 10

    base = base % 10

    if base == 1 or base == 5 or base == 6:
        remain = base

    elif base == 2 or base == 4 or base == 8:
        exp = exp % 4
        remain = 6 if exp == 0 else int(math.pow(base, exp) % 10)

    elif base == 3 or base == 7 or base == 9:
        exp = exp % 4
        remain = int(math.pow(base, exp) % 10)

    return remain


if __name__ == '__main__':
    main()
