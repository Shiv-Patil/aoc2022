treemap = []

while inp := input():
    treemap.append((*map(int, inp),))

cols = len(treemap[0])
rows = len(treemap)

scenic_scores = {}

for r in range(1, rows - 1):  # row-wise check
    for c in range(1, cols - 1):
        height = treemap[r][c]

        score, distance = 1, 0  # left
        for i in range(c - 1, -1, -1):
            distance += 1
            if height <= treemap[r][i]:
                break

        score, distance = score * distance, 0  # right
        for i in range(c + 1, cols):
            distance += 1
            if height <= treemap[r][i]:
                break

        score, distance = score * distance, 0  # top
        for i in range(r - 1, -1, -1):
            distance += 1
            if height <= treemap[i][c]:
                break

        score, distance = score * distance, 0  # bottom
        for i in range(r + 1, rows):
            distance += 1
            if height <= treemap[i][c]:
                break

        scenic_scores[(r, c)] = score * distance

print(max(scenic_scores.values()))
