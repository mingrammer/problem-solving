s = list(raw_input())
for i in range(len(s)): s[i] = s[i].upper() if s[i].islower() else s[i].lower()
print ''.join(s)
