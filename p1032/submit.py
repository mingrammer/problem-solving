import sys
r = lambda: sys.stdin.readline()
n = int(r().split()[0])

cmd_set = []
pattern = []
is_match = True

for i in range(0, n):
    cmd_set.append((lambda: sys.stdin.readline())())

for i in range(0, len(cmd_set[0])):
    for j in range(1, n):
        if cmd_set[0][i] != cmd_set[j][i]:
            pattern.append("?")
            is_match = False
            break

    if is_match:
        pattern.append(cmd_set[0][i])

    is_match = True


print ''.join(pattern)
