# Maximum path sum 2

with open('data/p067_triangle.txt', 'r') as f:
    triangle = f.read()

    triangle_leaves = []
    for line in triangle.strip().splitlines():
        triangle_leaves.append([int(i) for i in line.split()])

    n = len(triangle_leaves)
    for i, leaves in enumerate(triangle_leaves[-2::-1]):
        for j, leaf in enumerate(leaves):
            left = triangle_leaves[n-i-1][j]
            right = triangle_leaves[n-i-1][j+1]
            triangle_leaves[n-i-2][j] += max(left, right)

    print(triangle_leaves[0][0])
