m, i = 0, 0
for e in range(5):
    s = sum(map(int, raw_input().split()))
    if m < s: m = s; i = e+1
print i, m
