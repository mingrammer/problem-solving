s = [raw_input().split() for _ in range(9)]
print s
i, j, m = 0, 0, 0
for p,q in enumerate(s):
    for t,r in enumerate(q):
        r = int(r)
        if m < r: m = r; i = p; j = t
print m
print i+1, j+1
