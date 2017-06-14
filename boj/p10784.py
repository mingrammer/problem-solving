from math import sin, cos
p, a, b, c, d, n = map(int, raw_input().split())
s = []
r = []
m = 0
for k in range(1, n+1):
    s.append(p*(sin(a*k+b) + cos(c*k+d) + 2))
#
