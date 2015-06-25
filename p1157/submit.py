alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

word = raw_input().upper()

counts = [word.count(i) for i in alpha]

m = max(counts)

print alpha[counts.index(m)] if counts.count(m) == 1 else "?"
