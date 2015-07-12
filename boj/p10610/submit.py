n = sorted(raw_input())
if (sum(map(int,n)) % 3 != 0) or (n[0] != '0'): print -1
else: print ''.join(n[::-1])
