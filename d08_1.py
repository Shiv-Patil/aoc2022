treemap = []
visible = set()  # other than boundry

while inp := input():
    treemap.append((*map(int, inp),))

cols = len(treemap[0])
rows = len(treemap)

for r in range(1, rows - 1):  # row-wise check
    leftmax = treemap[r][0]
    rightmax = treemap[r][-1]

    possibly_visible_from_right = {}
    min_possible_right = rightmax

    for c in range(1, cols - 1):
        height = treemap[r][c]
        if height > leftmax:
            leftmax = height
            visible.add((r, c))
        elif height > rightmax:
            possibly_visible_from_right[(r, c)] = height
            if height < min_possible_right:
                min_possible_right = height
            else:
                possibly_visible_from_right = {
                    k: v
                    for k, v in possibly_visible_from_right.items()
                    if v > height or k == (r, c)
                }
                min_possible_right = min(possibly_visible_from_right.values())

    visible = visible.union(possibly_visible_from_right)

for c in range(1, cols - 1):  # column-wise check
    topmax = treemap[0][c]
    bottommax = treemap[-1][c]

    possibly_visible_from_bottom = {}
    min_possible_bottom = bottommax

    for r in range(1, rows - 1):
        height = treemap[r][c]
        if height > topmax:
            topmax = height
            visible.add((r, c))
        elif height > bottommax:
            possibly_visible_from_bottom[(r, c)] = height
            if height < min_possible_bottom:
                min_possible_bottom = height
            else:
                possibly_visible_from_bottom = {
                    k: v
                    for k, v in possibly_visible_from_bottom.items()
                    if v > height or k == (r, c)
                }
                min_possible_bottom = min(possibly_visible_from_bottom.values())

    visible = visible.union(possibly_visible_from_bottom)

print(len(visible) + 2 * rows + 2 * cols - 4)
