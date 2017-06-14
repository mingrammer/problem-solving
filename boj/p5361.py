p = [350.34, 230.90, 190.55, 125.30, 180.90]
for _ in range(input()):
    n = map(int, raw_input().split())
    s = sum([i*j for i, j in zip(p, n)])
    print "$%.2f" % s
