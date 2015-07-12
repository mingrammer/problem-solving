r = lambda: map(int, raw_input().split(':'))
c, i, t = r(), r(), 0

for k in range(3): t += (i[k]-c[k])*60**(2-k)
if t < 0: t += 86400

h = t/3600; t -= h*3600
m = t/60; t -= m*60
s = t

if h==m==s==0: print '24:00:00'
else: print '%.2d:%.2d:%.2d' % (h, m, s)
