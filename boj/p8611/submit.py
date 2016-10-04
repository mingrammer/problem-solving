n = input()
f = False
for i in range(2, 11):
    t = n
    j = 0
    s = []
    while t > 0:
        s.append(str(t % i))
        t /= i
    s = ''.join(s)
    if s == s[::-1]:
        print i, s[::-1]
        f = True

if not f:
    print 'NIE'
