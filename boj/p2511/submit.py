r = lambda: map(int, raw_input().split())
a, b = r(), r()

m, n, s = 0, 0, 0
c = 0

for i, j in zip(a, b):
    if i > j: m += 3; c = 1
    elif i == j: s += 1
    else: n += 3; c = 0

print m+s, n+s

if m > n: print 'A'
elif s == 10: print 'D'
elif m == n: print 'A' if c else 'B'
else: print 'B'
