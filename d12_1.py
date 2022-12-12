from collections import deque, defaultdict

heightmap = []

i = 0
while inp := input():
    line = []
    for j, c in enumerate(inp):
        if c == "S":
            c = "a"
            si, sj = i, j
        if c == "E":
            ei, ej = i, j
            c = "z"
        line.append(ord(c) - ord("a"))
    heightmap.append(line)
    i += 1

rows = len(heightmap)
cols = len(heightmap[0])
total = rows * cols

locs = deque([(si, sj)])
steps = defaultdict(lambda: total)
steps[si, sj] = 0
reached_in_steps = []

directions = ((0, -1), (-1, 0), (0, 1), (1, 0))
while len(locs):
    ci, cj = locs.popleft()
    for di, dj in directions:
        ni, nj = ci + di, cj + dj
        if (
            (ni >= 0 and ni < rows)
            and (nj >= 0 and nj < cols)
            and (heightmap[ni][nj] - heightmap[ci][cj] <= 1)
            and (steps[ci, cj] + 1 < steps[ni, nj])
        ):
            if (ni, nj) == (ei, ej):
                reached_in_steps.append(steps[ci, cj] + 1)
                continue
            locs.append((ni, nj))
            steps[ni, nj] = steps[ci, cj] + 1

print("Fewest steps required =", min(reached_in_steps))
