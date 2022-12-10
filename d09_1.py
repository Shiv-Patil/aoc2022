visited = {(0, 0)}

head = (0, 0)  # (row, column); NOT x, y
tail = (0, 0)


def move(head, tail, visited):
    vertical_sep = head[0] - tail[0]
    horizontal_sep = head[1] - tail[1]

    if (vertical_sep**2 + horizontal_sep**2) > 2:
        tail = (
            (head[0], tail[1])
            if abs(vertical_sep) == 1
            else (head[0] - vertical_sep // abs(vertical_sep), tail[1])
            if abs(vertical_sep) > 1
            else tail
        )
        tail = (
            (tail[0], head[1])
            if abs(horizontal_sep) == 1
            else (tail[0], head[1] - horizontal_sep // abs(horizontal_sep))
            if abs(horizontal_sep) > 1
            else tail
        )
        visited.add(tail)
    return tail


while inp := input():
    direction, steps = inp.split()
    steps = int(steps)
    for step in range(steps):
        if direction in ("R", "L"):
            head = (head[0], head[1] + (1 if direction == "R" else -1))
        else:
            head = (head[0] + (1 if direction == "U" else -1), head[1])
        tail = move(head, tail, visited)

print(len(visited))
