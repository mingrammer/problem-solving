height_list = []
dwarf_height_list = []

for i in range(9):
    height_list.append(int(input()))

height_list.sort()

sum_remain_heights = sum(height_list) - 100

for height in height_list:
    pair = sum_remain_heights - height

    if pair in height_list:
        height_list.remove(height)
        height_list.remove(pair)
        break

for height in height_list:
    print(height)
