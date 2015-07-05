n = input(); i = 1
while i < 2*n: print " "*(i-1) + "*"*(2*(n-i)+1) if i < n else " "*(2*n-i-1) + "*"*(2*(i-n)+1); i += 1
