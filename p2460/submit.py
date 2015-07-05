t, m = 0, 0
for _ in range(10):
    o, i = map(int, raw_input().split())
    t += i-o
    if m < t: m = t
print m
