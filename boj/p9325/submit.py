for _ in range(input()):
    s = input()
    o = 0
    for _ in range(input()):
        q, p = map(int, raw_input().split())
        o += p*q
    print s + o
