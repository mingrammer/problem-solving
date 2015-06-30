for _ in range(input()):
    h, w = map(int, raw_input().split())
    for _ in range(h): print str(raw_input()[::-1])
