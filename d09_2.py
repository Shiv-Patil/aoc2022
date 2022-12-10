visited = {(0, 0)}

rope = [(0, 0)] * 10


def move(rope, visited):
    for t in range(1, len(rope)):
        head = rope[t - 1]
        tail = rope[t]
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
            rope[t] = tail

    visited.add(rope[-1])


while inp := input():
    direction, steps = inp.split()
    steps = int(steps)
    for step in range(steps):
        if direction in ("R", "L"):
            rope[0] = (rope[0][0], rope[0][1] + (1 if direction == "R" else -1))
        else:
            rope[0] = (rope[0][0] + (1 if direction == "U" else -1), rope[0][1])
        move(rope, visited)

print(len(visited))
