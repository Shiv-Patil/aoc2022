elves = []
while inp := input():
    elf = int(inp)
    while inp := input():
        elf += int(inp)
    elves.append(elf)
print(sum(sorted(elves)[-3:]))
