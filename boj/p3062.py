for _ in range(input()):
    n = raw_input()
    s = str(int(n) + int(n[::-1]))
    print 'YES' if s == s[::-1] else 'NO'
