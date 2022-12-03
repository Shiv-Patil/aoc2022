def priority(c):
    return(p) if (p := ord(c)-96) > 0 else p+58


total = 0
while (inp := input()):
    half = len(inp)//2
    c1, c2 = set(inp[:half]), set(inp[half:])
    total += priority(list(c1 & c2)[0])

print(total)
