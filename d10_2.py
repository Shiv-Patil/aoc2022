x = 1
wait = False
screen_width = 40
screen_height = 6
CRT = ["."] * (screen_width * screen_height)
for cycle, pixel in enumerate(CRT, 1):
    line = cycle // screen_width
    if cycle - (line * screen_width) in range(x, x + 3):
        CRT[cycle - 1] = "#"
    if not wait:
        inp = input()
        if inp == "noop":
            continue
        elif not inp:
            break
        addx = int(inp.split()[1])
        wait = True
        continue
    wait = False
    x += addx

for i in range(0, screen_width * screen_height, screen_width):
    print("".join(CRT[i : i + screen_width]))
