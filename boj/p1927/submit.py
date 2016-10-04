s = []
for _ in range(input()):
    m = input()
    if m:
        s.append(m)
    else:
        if s:
            s.sort(reverse=True)
            print s.pop()
        else:
            print 0
