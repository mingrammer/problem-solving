t, c  = 0, 0
n = input()
s = [n-p for p in range(n)]
for i in range(n):
    c = 0
    for j in range(n-i-1):
        if s[j] > s[j+1]: t = s[j]; s[j]=s[j+1]; s[j+1]=t; c=1
    if not c: break
print i+1
