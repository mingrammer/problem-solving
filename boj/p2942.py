from fractions import gcd

r, g = map(int, raw_input().split())

m = gcd(r, g)
n = set([])

d = 0

while d**2 <= m:
    d += 1
    if m % d != 0: continue
    n.add(d); n.add(m/d)

for i in n:
    print i, r/i, g/i
