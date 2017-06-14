s = [input() for _ in range(10)]
n = 0

for i in range(10):
    n = sum(s[:i])
    if (100-n)*(100-(n+s[i])) <= 0: break
print n if abs(100-n) < abs(100-(n+s[i])) else n+s[i]
