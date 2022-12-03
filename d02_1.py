total = 0
shapes = {"X": 1, "Y": 2, "Z": 3}
outcomes = {"AZ": 0, "BX": 0, "CY": 0, "AX": 3,
            "BY": 3, "CZ": 3, "AY": 6, "BZ": 6, "CX": 6}
while inp := input():
    opp, you = inp.split()
    total += shapes.get(you)
    total += outcomes.get(opp+you)

print(total)
