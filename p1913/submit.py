n = input()
v = input()

s = n**2

snail = [[0 for i in range(0, n)] for j in range(0, n)]

dir_down = dir_right = -1
row = -1
col = 0

move = n

while True:
    dir_down *= -1
    dir_right *= -1

    for i in range(0, move):
        row += dir_down
        snail[row][col] = s
        s -= 1

    if s == 0: break
    move -= 1

    for i in range(0, move):
        col += dir_right
        snail[row][col] = s
        s -= 1

for i in range(0, n):
    for j in range(0, n):
        print snail[i][j],
        if snail[i][j] == v:
            row = i + 1
            col = j + 1
    print ""

print row, col
