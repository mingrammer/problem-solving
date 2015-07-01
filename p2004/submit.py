n, m = map(int, raw_input().split())

p, q = 0, 0

for i in range(30):
    r = 2**(i+1)
    s = 5**(i+1)

    p += n / r - m / r - (n-m) / r
    q += n / s - m / s - (n-m) / s

print q if p > q else p
