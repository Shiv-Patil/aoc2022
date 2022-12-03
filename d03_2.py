def priority(c):
    return(p) if (p := ord(c)-96) > 0 else p+58


total = 0
while (inp := input()):
    rs1 = set(inp)
    rs2, rs3 = set(input()), set(input())
    total += priority(list(rs1 & rs2 & rs3)[0])

print(total)
