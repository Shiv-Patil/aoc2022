import sys

sys.setrecursionlimit(15000)

data = [
    line[1:-1]
    for line in open("24.in", "r").read().strip().split("\n")[1:-1]
]
width, height = len(data[0]), len(data)
blizzards = {}

for r, line in enumerate(data):
    for c, char in enumerate(line):
        r_distances = set()
        c_distances = set()
        for i in range(c, c + width):
            i = i % width
            if line[i] in ("<", ">"):
                r_distances.add(
                    (i - c if i >= c else width - c + i)
                    if line[i] == "<"
                    else (width - i + c if i > c else c - i)
                )
        for j in range(r, r + height):
            j = j % height
            if data[j][c] in ("v", "^"):
                c_distances.add(
                    (j - r if j >= r else height - r + j)
                    if data[j][c] == "^"
                    else (height - j + r if j > r else r - j)
                )
        blizzards[r, c] = (r_distances, c_distances)


def pathfind(time=0, cur=(-1, 0), rev=False):
    global reached_time
    cx, cy = cur
    start_time = (time % width, time % height)
    t = time + 1
    q = [(cx, cy + 1), (cx + 1, cy), (cx - 1, cy), (cx, cy - 1)][:: -1 if rev else 1]
    while (t % width, t % height) != start_time and len(q) and t < reached_time:
        for _ in range(len(q)):
            nr, nc = q.pop(0)
            if (abs(dx - nr) + abs(dy - nc)) > reached_time - t:
                return
            if (
                (nr, nc, start_time) in visited
                or nr < 0
                or nc < 0
                or nr >= height
                or nc >= width
            ):
                continue
            if not (
                t % width in blizzards.get((cx, cy), ([],))[0]
                or t % height in blizzards.get((cx, cy), (None, []))[1]
            ):
                q.append((nr, nc))
            if t % width in blizzards[nr, nc][0] or t % height in blizzards[nr, nc][1]:
                continue
            if (nr, nc) == (dx, dy):
                if t < reached_time:
                    reached_time = t
            visited.add((nr, nc, start_time))
            pathfind(t, (nr, nc), rev)
        t += 1


total_time = 0
for _ in range(3):
    reached_time = float("inf")
    visited = set()
    dx, dy = (height - 1, width - 1) if _ != 1 else (0, 0)
    pathfind(total_time, *(((height, width - 1), True) if _ == 1 else ((0, 0), False)))
    total_time = reached_time + 1
    print(total_time)

print(total_time)
