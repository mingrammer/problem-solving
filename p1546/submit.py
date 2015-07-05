n = input()
s = map(int, raw_input().split())
print '%.2f' % ((sum(s)*100.0/max(s))/n)
