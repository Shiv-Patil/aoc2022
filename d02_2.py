total = 0
outcomes = {"AX": 0+3, "BX": 0+1, "CX": 0+2, "AY": 3+1,
            "BY": 3+2, "CY": 3+3, "AZ": 6+2, "BZ": 6+3, "CZ": 6+1}
while inp := input():
    opp, out = inp.split()
    total += outcomes.get(opp+out)

print(total)
