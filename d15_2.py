# slow

from collections import defaultdict

cannot_contain = defaultdict(lambda: [])
maxrow = 4000000

while inp := input():
    (sx, sy), (bx, by) = map(
        lambda l: (*map(lambda ll: int(ll.split("=")[1]), l.split(",")),),
        inp.split(":"),
    )
    distance = abs(sx - bx) + abs(sy - by)
    for row in range(max(0, sy - distance), min(maxrow, sy + distance + 1)):
        ydiff = abs(row - sy)
        length = distance - ydiff
        cannot_contain[row].append((max(0, sx - length), min(maxrow, sx + length)))

for row, spaces in cannot_contain.items():
    spaces.sort()
    cstart, cstop = spaces.pop(0)
    final = [(cstart, cstop)]

    for start, stop in spaces:
        if start > cstop + 1:
            final.append((start, stop))
            cstart, cstop = start, stop
        else:
            cstop = max(cstop, stop)
            final[-1] = (cstart, cstop)

    if len(final) >= 2:
        print(row + (final[0][1] + 1) * 4000000)
        break
