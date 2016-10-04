m, n, r = 1, 1, 1

input()

for e in map(int, raw_input().split()):
    m *= e

input()

for e in map(int, raw_input().split()):
    n *= e

while m % n != 0 and n % m != 0:
    if m > n:
        m, n = m - (m / n) * n, n
    else:
        m, n = m, n - (n / m) * m
r = m if m < n else n

if len(str(r)) >= 9:
    print str(r)[-9:]
else:
    print r
