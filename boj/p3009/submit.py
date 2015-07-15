p = [map(int, raw_input().split()) for _ in range(3)]
m = [x[0] for x in p]
n = [y[1] for y in p]
x = min(m) if m.count(min(m))< 2 else max(m)
y = min(n) if n.count(min(n))< 2 else max(n)
print x, y
