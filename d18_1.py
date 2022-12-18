pos = {}
covered = 0
dirs = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))

while inp := input():
    x, y, z = map(int, inp.split(","))
    pos[x, y, z] = 1
    covered += sum((pos.get((x + i, y + j, z + k), 0) for i, j, k in dirs))

print(6 * len(pos) - 2 * covered)
