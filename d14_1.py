from collections import defaultdict

is_rock = defaultdict(lambda: False)
max_y = 1

while inp := input():
    lines = (*map(lambda x: (*map(int, x.split(",")),), inp.split(" -> ")),)
    for i in range(1, len(lines)):
        old_x, new_x = lines[i - 1][0], lines[i][0]
        step_x = (new_x - old_x) // abs(new_x - old_x) if new_x - old_x else 1
        old_y, new_y = lines[i - 1][1], lines[i][1]
        step_y = (new_y - old_y) // abs(new_y - old_y) if new_y - old_y else 1
        for x in range(old_x, new_x + step_x, step_x):
            is_rock[x, new_y] = True
        for y in range(old_y, new_y + step_y, step_y):
            is_rock[new_x, y] = True
        if old_y > max_y:
            max_y = old_y

rested = 0
cx, cy = 500, 0
path = []
while True:
    ny = cy + 1
    if (
        dx := (not is_rock[cx, ny])
        or (not is_rock[cx - 1, ny] and -1)
        or (not is_rock[cx + 1, ny] and +1)
    ):
        nx = cx + (dx if dx is not True else 0)
        path.append((cx, cy))
        cx, cy = nx, ny
    else:
        rested += 1
        is_rock[cx, cy] = True
        cx, cy = path.pop()
        continue
    if cy >= max_y:
        break

print(rested)
