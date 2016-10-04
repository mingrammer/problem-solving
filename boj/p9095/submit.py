for _ in range(input()):
    a, b, c = 0, 0, 1
    for _ in range(input()): a, b, c = b, c, a+b+c
    print c
