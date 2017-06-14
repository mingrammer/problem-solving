x, y, w, h = map(int, raw_input().split())
print min(x, y, w-x, h-y)
