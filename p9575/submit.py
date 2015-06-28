def check(s):
    for c in s:
        if c not in '58': return -1
    return s

for _ in range(input()):
    r = lambda: set(map(int, raw_input().split()))

    r(); a = r()
    r(); b = r()
    r(); c = r()

    nums = set(check(str(i+j+k)) for i in a for j in b for k in c)
    nums.discard(-1)

    print len(nums)
