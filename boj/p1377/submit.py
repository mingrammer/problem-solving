nums = [input() for _ in range(input())]

s_nums = sorted(nums)
s_nums_dict = {}
c = 0

for i, n in enumerate(s_nums):
    s_nums_dict[n] = i

for i, n in enumerate(nums):
    if s_nums_dict[n] < i:
	d = i - s_nums_dict[n]
	if d > c:
	    c = d

print c + 1
	
