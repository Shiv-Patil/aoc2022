SNAFU = {
    5: ("1", "0"),
    4: ("1", "-"),
    3: ("1", "="),
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2,
    -3: ("-", "2"),
    -4: ("-", "1"),
    -5: ("-", "0"),
}
data = open("25.in", "r").read().strip().split("\n")

cur = data.pop()
carry = "0"
for num in data:
    if len(cur) > len(num):
        num = num.rjust(len(cur), "0")
    elif len(num) > len(cur):
        cur = cur.rjust(len(num), "0")
    else:
        num = num.rjust(len(num) + 1, "0")
        cur = cur.rjust(len(cur) + 1, "0")

    res = ""
    for c in range(-1, -len(cur) - 1, -1):
        addition = SNAFU[cur[c]] + SNAFU[num[c]] + SNAFU[carry]
        carry, next = SNAFU.get(
            addition,
            ("0", str(addition) if addition >= 0 else "-" if addition == -1 else "="),
        )
        res = next + res
    cur = res.lstrip("0")

print(cur)
