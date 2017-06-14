n = raw_input()
ns = set(raw_input().split())
m = raw_input()
ms = raw_input().split()

for e in ms: print int(e in ns)
