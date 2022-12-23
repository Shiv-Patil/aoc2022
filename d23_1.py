data = open("23.in", "r").read().split("\n")

cur_map = {}

for r, inp in enumerate(data):
    for c, v in enumerate(inp):
        if v == "#":
            cur_map[r, c] = True

consider = (
    lambda round, n: ("N", "S", "W", "E")[((round % 4) + n) % 4] if n < 4 else False
)


def get_dirs(pos, d):
    dp, di = d in ("E", "W"), (1, -1)[d in ("N", "W")]
    pos = pos[:: -1 if dp else 1]
    x = pos[0] + di
    return [(x, pos[1] + p)[:: -1 if dp else 1] for p in range(-1, 2)]


def get_adjavent_squares(pos):
    return [
        (pos[0] + i, pos[1] + j)
        for i in range(-1, 2)
        for j in range(-1, 2)
        if (i, j) != (0, 0)
    ]


for round in range(10):
    next_positions = {}
    num_elves_considering = {}
    new_map = {}
    for elf in cur_map:
        if not cur_map[elf]:
            continue
        if any((cur_map.get(p, False) for p in get_adjavent_squares(elf))):
            n = 0
            while True:
                d = consider(round, n)
                if not d:
                    break
                dirs = get_dirs(elf, d)
                if any((cur_map.get(p, None) for p in dirs)):
                    n += 1
                    continue
                num_elves_considering[dirs[1]] = (
                    num_elves_considering.get(dirs[1], 0) + 1
                )
                next_positions[elf] = dirs[1]
                break
    for cur_pos in cur_map:
        if not cur_pos in next_positions:
            if cur_map[cur_pos]:
                new_map[cur_pos] = True
            continue
        next_pos = next_positions[cur_pos]
        if num_elves_considering.get(next_pos) > 1:
            new_map[cur_pos] = True
            continue
        new_map[next_pos] = True
    cur_map = new_map.copy()

print(
    (max(cur_map)[0] - min(cur_map)[0] + 1)
    * (max(cur_map, key=lambda x: x[1])[1] - min(cur_map, key=lambda x: x[1])[1] + 1)
    - len(cur_map)
)
