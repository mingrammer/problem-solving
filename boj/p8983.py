r = lambda: map(int, raw_input().split())
m, n, l = r()
x = [i for i in range(m)] #r()
s = [[k+1000000000,k+1000000000] for k in range(n)] #[r() for _ in range(n)]
c = 0
s = sorted(s, key=lambda e: e[0]+e[1])
t = list(s)

for i in x:
    for j in s:
        if (j[0]+j[1] <= i+l):
            if (j[0]-j[1] >= i-l): c+=1; t.remove(j);
        else: break
    s = list(t)
    if s is None: break
print c
