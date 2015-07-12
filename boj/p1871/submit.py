apb = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for _ in range(input()):
    l, d = raw_input().split('-')
    r = abs(sum([apb.index(l[i])*(26**(2-i))for i in range(3)]) - int(d))
    print 'nice' if r <= 100 else 'not nice'
