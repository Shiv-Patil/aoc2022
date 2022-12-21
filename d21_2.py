from collections import defaultdict

monkeys = {}
callbacks = defaultdict(set)


def operate(a, o, b):
    return {"+": a + b, "-": a - b, "*": a * b, "/": a // b}[o]


def yell(m, m1, op, m2):
    m1_yells, m2_yells = monkeys.get(m1), monkeys.get(m2)
    if isinstance(m1_yells, int) and isinstance(m2_yells, int):
        monkeys[m] = operate(m1_yells, op, m2_yells)
        return [yell(x, *monkeys[x]) for x in tuple(callbacks[m]) if x != "humn"]
    if not isinstance(m1_yells, int):
        callbacks[m1] |= {m}
    if not isinstance(m2_yells, int):
        callbacks[m2] |= {m}
    monkeys[m] = (m1, op, m2)


while inp := input():
    m, yells = inp.split(": ")
    if m == "humn":
        monkeys[m] = ("human", None, None)
        continue
    if yells.isdigit():
        monkeys[m] = int(yells)
        [yell(x, *monkeys[x]) for x in tuple(callbacks[m]) if x != "humn"]
        continue
    yell(m, *yells.split())


def un_yell(m1, op, m2, val):
    m1_yells, m2_yells = monkeys.get(m1), monkeys.get(m2)
    if m1 == "human":
        return print(val)
    if op == "+":
        un_yell(
            *(
                (*m2_yells, val - m1_yells)
                if isinstance(m1_yells, int)
                else (*m1_yells, val - m2_yells)
            )
        )
    elif op == "-":
        un_yell(
            *(
                (*m2_yells, m1_yells - val)
                if isinstance(m1_yells, int)
                else (*m1_yells, val + m2_yells)
            )
        )
    elif op == "*":
        un_yell(
            *(
                (*m2_yells, val // m1_yells)
                if isinstance(m1_yells, int)
                else (*m1_yells, val // m2_yells)
            )
        )
    elif op == "/":
        un_yell(
            *(
                (*m2_yells, m1_yells // val)
                if isinstance(m1_yells, int)
                else (*m1_yells, val * m2_yells)
            )
        )


_m1, _op, _m2 = monkeys["root"]
known, unknown = (_m1, _m2) if isinstance(monkeys.get(_m1), int) else (_m2, _m1)
un_yell(*monkeys.get(unknown), monkeys.get(known))
