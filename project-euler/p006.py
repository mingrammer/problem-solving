# Sum square difference

n, s = 100, 0
for i in range(n):
    s += (i+1)**2
print((n*(n+1)/2)**2 - s)
