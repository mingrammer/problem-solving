n =  input()
m = map(int, raw_input().split())
s = [0]*n
for i in range(n):
    s[m[i]-1] = m[i] - (i+1)
for i in range(n):
    print s[i]
