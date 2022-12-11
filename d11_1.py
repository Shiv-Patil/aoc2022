class Monkey:
    items_inspected = 0

    def __init__(
        self, starting_items: "tuple[int]", operation: str, test: "tuple[str, int, int]"
    ):
        self.items = list(starting_items)
        self._set_operation(operation)
        self._set_test(*test)

    def _set_operation(self, string: str):
        op1, opr, op2 = string.split("=")[1].split()
        get_op1 = lambda x: x if op1 == "old" else int(op1)
        get_op2 = lambda x: x if op2 == "old" else int(op2)
        self.inspect = (
            (lambda old: get_op1(old) + get_op2(old))
            if opr == "+"
            else (lambda old: get_op1(old) * get_op2(old))
        )

    def _set_test(self, string: str, true: int, false: int):
        divisor = int(string.split()[2])
        self.test = lambda x: true if x % divisor == 0 else false

    def play_turn(self, monkeys: "list[Monkey]"):
        while len(self.items):
            item = self.items.pop(0)
            item = self.inspect(item) // 3
            self.items_inspected += 1
            throw_to = self.test(item)
            monkeys[throw_to].items.append(item)


monkeys: "list[Monkey]" = []
while inp := input():
    starting_items = (*map(int, input().split(":")[1].split(",")),)
    operation_string = input().split(":")[1]
    test_string = input().split(":")[1]
    test_true = int(input().split()[-1])
    test_false = int(input().split()[-1])
    input()
    monkeys.append(
        Monkey(starting_items, operation_string, (test_string, test_true, test_false))
    )

rounds = 20
for round in range(rounds):
    for monkey in monkeys:
        monkey.play_turn(monkeys)

inspections = []
print(f"In {rounds} rounds:\n")
for mid in range(len(monkeys)):
    inspections.append((mid, monkeys[mid].items_inspected))
    print(f"Monkey {mid} inspected items {monkeys[mid].items_inspected} times.")
print()

inspections.sort(key=lambda x: x[1])

most_active_1 = inspections.pop()
print(
    f"Monkey {most_active_1[0]} was the --first---- most active with {most_active_1[1]} inspections."
)

most_active_2 = inspections.pop()
print(
    f"Monkey {most_active_2[0]} was the --second--- most active with {most_active_2[1]} inspections.\n"
)

business_level = most_active_1[1] * most_active_2[1]
print(f"The monkey business level was {business_level}.")
