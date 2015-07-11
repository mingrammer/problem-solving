def next(m, s, n):

    if m==n: return s

    c = [[" "]*(3*m) for _ in range(3*m)]

    for i in range(m):
        for j in range(m):
            for k in range(3):
                for l in range(3):
                    a, b = i+k*m, j+l*m
                    if not (a > m-1 and a < 2*m and b > m-1 and b < 2*m): c[a][b] = s[i][j]
    return next(3*m, c, n)

for e in next(1, ["*"], input()):
    print ''.join(e)
