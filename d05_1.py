crates = []
inputlines = []
while True:
    inp = input()
    if inp[1] == "1":
        linewidth = len(inp)
        input()
        break
    else:
        inputlines.append(inp)

for inp in inputlines:
    inp.ljust(linewidth)
    crates.append([(inp[i:i+3]) for i in range(0, linewidth, 4)])

stacks = []
for i in range(len(crates[0])):
    stack = []
    for ri in range(-1, -len(crates)-1, -1):
        if crates[ri][i] != "   ":
            stack.append(crates[ri][i])
    stacks.append(stack)

while inp := input():
    inps = inp.split()
    n, fro, to = int(inps[1]), int(inps[3])-1, int(inps[5])-1
    to_shift = stacks[fro][-n:][::-1]
    stacks[fro] = stacks[fro][:-n]
    stacks[to] += to_shift

print(''.join((i[-1][1] if len(i) else '' for i in stacks)))
