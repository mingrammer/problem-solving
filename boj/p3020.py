n, h = map(int, raw_input().split())
s = [k for k in range(n)]  #[input() for _ in range(n)]
b, r_b = s[0:n:2], 0
t, r_t = s[1:n:2], 0
m, c, r = 200001, 0, 0

for i in range(len(t)):
    t[i] = h - t[i]

b.sort()
t.sort()

for i in range(h):
    r = r_t
    for e in b[r_b:n / 2]:
        if e >= i + 1:
            if e == i + 1:
                r_b = b.index(e)
            r += 1
    for e in t[r_t:n / 2]:
        if e < i + 1:
            r += 1
        else:
            r_t = t.index(e)
    if m > r:
        m = r
        c = 1
        continue
    elif m == r:
        c += 1

print m, c
