r = lambda:  map(int, raw_input().split())
n, m = r(); a = r()
i, k, s = 0, 0, 0
for e in a:
    s += e
    while s > m: s -= a[i]; i += 1
    if s == m: k += 1
print k
