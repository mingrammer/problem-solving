from math import factorial as f

for _ in range(input()):
    n, m = map(int, raw_input().split())

    print f(m) / (f(n) * f(m-n))
