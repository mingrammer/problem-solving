n, m = map(int, raw_input().split())

mat = [map(int, raw_input().split()) for _ in range(n)]

for _ in range(input()):
    i, j, x, y = map(int, raw_input().split()) 
    s = 0

    for k in range(x-i+1):
	s += sum(mat[i+k-1][j-1:y]) 

    print s 
