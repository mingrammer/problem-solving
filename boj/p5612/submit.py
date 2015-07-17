n, s, m = input(), input(), 0
for _ in range(n):
    c = map(int, raw_input().split())
    s += c[0]-c[1]
    if s < 0: print 0; break
    if m < s: m = s
else: print m
