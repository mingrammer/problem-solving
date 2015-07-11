while True:
    a, b = map(int, raw_input().split())
    if a == 0: break
    print 'Yes' if a > b else 'No'
