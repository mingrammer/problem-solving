import math
n, w, h = map(int, raw_input().split())
for _ in range(n):
    print 'DA' if input() <= math.hypot(w, h) else 'NE'
