s = map(int, raw_input().split())
if s == range(1, 9): print "ascending"
elif s == range(8, 0, -1): print "descending"
else: print "mixed"
