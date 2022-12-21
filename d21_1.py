from collections import defaultdict

monkeys = {}
callbacks = defaultdict(set)


def operate(a, o, b):
    return {"+": a + b, "-": a - b, "*": a * b, "/": a // b}[o]


def yell(m, m1, op, m2):
    m1_yells, m2_yells = monkeys.get(m1), monkeys.get(m2)
    if isinstance(m1_yells, int) and isinstance(m2_yells, int):
        monkeys[m] = operate(m1_yells, op, m2_yells)
        return [yell(x, *monkeys[x]) for x in tuple(callbacks[m])]
    if not isinstance(m1_yells, int):
        callbacks[m1] |= {m}
    if not isinstance(m2_yells, int):
        callbacks[m2] |= {m}
    monkeys[m] = (m1, op, m2)


while inp := input():
    m, yells = inp.split(": ")
    if yells.isdigit():
        monkeys[m] = int(yells)
        [yell(x, *monkeys[x]) for x in tuple(callbacks[m])]
        continue
    yell(m, *yells.split())

print(monkeys["root"])
