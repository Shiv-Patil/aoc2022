cannot_contain = []
row = 2000000

while inp := input():
    (sx, sy), (bx, by) = map(
        lambda l: (*map(lambda ll: int(ll.split("=")[1]), l.split(",")),),
        inp.split(":"),
    )
    distance = abs(sx - bx) + abs(sy - by)
    ydiff = abs(row - sy)
    if ydiff > distance:
        continue
    length = distance - ydiff
    cannot_contain.append((sx - length, sx + length))

cannot_contain.sort()
cstart, cstop = cannot_contain.pop(0)
final = [(cstart, cstop)]

for start, stop in cannot_contain:
    if start > cstop:
        final.append((start, stop))
        cstart, cstop = start, stop
    else:
        cstop = max(cstop, stop)
        final[-1] = (cstart, cstop)

print(sum((i[1] - i[0] for i in final)))
