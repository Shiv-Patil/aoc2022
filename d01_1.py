most = 0
while inp := input():
    elf = [int(inp)]
    while inp := input():
        elf.append(int(inp))
    most = max(most, sum(elf))
print(most)
