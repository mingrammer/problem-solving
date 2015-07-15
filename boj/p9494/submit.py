while True:
    n = input()

    if n == 0: break

    txt = [raw_input() for _ in range(n)]

    pos = 0

    for t in txt:
        if len(t) > pos:
            pos += t[pos:].find(' ') if t[pos:].find(' ') > -1 else len(t[pos:])

    print pos + 1
