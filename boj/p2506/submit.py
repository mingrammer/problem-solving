input()
print sum(len(s)*(len(s)+1)/2  for s in raw_input().replace(' ','').split('0') if '1' in s)
