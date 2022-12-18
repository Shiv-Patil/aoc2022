from collections import namedtuple

Rock = namedtuple("Rock", "width height cols")
chamber_width = 7
rock_start_y = 3
rock_start_x = 2

rock_shapes = (
    ((1,), (1,), (1,), (1,)),
    ((0, 1, 0), (1, 1, 1), (0, 1, 0)),
    ((1, 0, 0), (1, 0, 0), (1, 1, 1)),
    ((1, 1, 1, 1),),
    ((1, 1), (1, 1)),
)
num_rocks = len(rock_shapes)
rocks = (*(Rock(len(shape), len(shape[0]), shape) for shape in rock_shapes),)

jet_pattern = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
num_jets = len(jet_pattern)


def get_rock(n):
    return rocks[n % num_rocks]


def get_jet(n):
    return jet_pattern[n % num_jets]


def apply_jet(rock, jet, left_x, area):
    left_x_new = left_x + (1, -1)[jet == "<"]
    n_rows = len(area)
    if left_x_new < 0 or left_x_new + rock.width > chamber_width:
        return left_x
    elif n_rows:
        for c in range(len(rock.cols)):
            for r in range(len(rock.cols[c])):
                if rock.cols[c][r] and (area[r][c + left_x_new] if n_rows > r else 0):
                    return left_x
    return left_x_new


def fall(rock, bottom_y, left_x, area):
    if bottom_y < 1:
        return bottom_y
    n_rows = len(area)
    if n_rows:
        for c in range(len(rock.cols)):
            for r in range(len(rock.cols[c])):
                if rock.cols[c][r] and (area[r][c + left_x] if n_rows > r else 0):
                    return bottom_y
    return bottom_y - 1


def land(rock, left_x, area):
    n_rows = len(area)
    r_cols = len(rock.cols)
    return (
        *(
            (
                *(
                    (area[r][c] if n_rows > r else 0)
                    or (
                        rock.cols[c - left_x][r]
                        if c - left_x < r_cols and c - left_x >= 0
                        else 0
                    )
                    for c in range(chamber_width)
                ),
            )
            for r in range(rock.height)
        ),
    )


total = 1e12
max_cycle_check = num_jets * num_rocks * 10
chamber = []
max_height = 0
cache = {}
turn = 0
for rock_n in range(max_cycle_check):
    bottom_y = max_height + rock_start_y
    left_x = rock_start_x
    falling = True
    c_key = (rock_n % num_rocks, turn % num_jets)
    if c_key in cache:
        rn, height = cache[c_key]
        cycles, left = divmod(1e12 - rock_n, rn - rock_n)
        if not left:
            print(max_height + (height - max_height) * int(cycles))
            break
    else:
        cache[c_key] = rock_n, max_height

    while falling:
        rock = get_rock(rock_n)
        jet = get_jet(turn)
        left_x = apply_jet(
            rock, jet, left_x, chamber[bottom_y : bottom_y + rock.height]
        )
        new_bottom_y = fall(
            rock, bottom_y, left_x, chamber[bottom_y - 1 : bottom_y - 1 + rock.height]
        )
        if new_bottom_y == bottom_y:
            falling = False
            if new_bottom_y + rock.height > max_height:
                max_height = new_bottom_y + rock.height
            chamber[new_bottom_y : new_bottom_y + rock.height] = land(
                rock, left_x, chamber[new_bottom_y : new_bottom_y + rock.height]
            )
            if rock_n >= total:
                print(max_height)
                break
        else:
            bottom_y = new_bottom_y
        turn += 1
else:
    print("Couldn't find a cycle. Try lowering total rocks.")
