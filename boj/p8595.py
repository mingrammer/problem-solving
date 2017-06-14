import re
input()
print sum(map(int, re.findall(r'\d+', raw_input())))
