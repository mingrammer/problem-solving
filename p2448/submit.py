p = input()

def next(m, s, n):

    if m==n: return s

    c = [[" "]*(2*i+1) for i in range(2*m)]

    for j in range(m):
            c[0+j] = s[0+j]
            c[m+j][0:] = s[0+j] + [" "]*(2*(m-j)-1)
            c[m+j][2*m:] = s[0+j]
    return next(2*m, c, n)

for i, e in enumerate(next(3, [["*"], ["* *"], ["*****"]], p)):
    print " "*(p-i-1) + ''.join(e) + " "*(p-i)
