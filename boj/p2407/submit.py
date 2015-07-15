from math import factorial as f

n, m = map(int, raw_input().split())

print f(n) / (f(m)*f(n-m))
