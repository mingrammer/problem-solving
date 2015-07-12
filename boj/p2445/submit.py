n = input(); i = 1
while i < 2*n: print "*"*i + " "*2*(n-i) + "*"*i if i < n else "*"*(2*n-i) + " "*2*(i-n) + "*"*(2*n-i); i += 1
