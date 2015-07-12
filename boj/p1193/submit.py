n, k = input(), 1
while k*(k+1)/2 < n: k+=1
r = k*(k+1)/2 - n
t, d = (r+1, k-r), k%2
print '%d/%d'%(t[1-d],t[d])
