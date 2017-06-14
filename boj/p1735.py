from fractions import gcd

r = lambda: map(int, raw_input().split())
a, b = r()
c, d = r()
m, n = a*d+b*c, b*d
g = gcd(m, n)

print m/g, n/g
