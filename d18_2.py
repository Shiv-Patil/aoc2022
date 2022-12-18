filled = set()
dirs = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
max_x = 0
max_y = 0
max_z = 0

while inp := input():
    x, y, z = map(int, inp.split(","))
    filled.add((x, y, z))
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    max_z = max(max_z, z)

bounds = (max_x + 1, max_y + 1, max_z + 1)
queue = [(-1, -1, -1)]
visited = set()

while len(queue):
    x, y, z = queue.pop()
    for p in {(x + i, y + j, z + k) for i, j, k in dirs} - filled - visited:
        if all(-1 <= c <= m for c, m in zip(p, bounds)):
            queue.append(p)
    visited.add((x, y, z))

covered = 0
for x, y, z in filled:
    for nx, ny, nz in ((x + i, y + j, z + k) for i, j, k in dirs):
        if (nx, ny, nz) in visited:
            covered += 1

print(covered)
