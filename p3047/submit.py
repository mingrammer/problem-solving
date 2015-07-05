s = map(int, raw_input().split()); s.sort()
o = raw_input()
d = {'A': s[0], 'B': s[1], 'C': s[2]}
for e in o: print d.get(e),
