n = input(); i = 1
while i < 2*n: print " "*(n-i) + "*"*(2*i-1) if i < n else " "*(i-n) + "*"*(2*(2*n-i)-1); i += 1
