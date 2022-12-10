cycle = 0
x = 1
breakpoints = (20, 60, 100, 140, 180, 220)
wait = False
total = 0
while True:
    cycle += 1
    if cycle in breakpoints:
        total += cycle * x
    if not wait:
        inp = input()
        if inp == "noop":
            continue
        elif not inp:
            cycle -= 1
            break
        addx = int(inp.split()[1])
        wait = True
        continue
    wait = False
    x += addx

print(x, cycle, total)
