from collections import defaultdict


class Valve:
    def __init__(self, label: str, flow_rate: int, connects: "list[int]"):
        self.label = label
        self.flow_rate = flow_rate
        self.connects = connects

    def does_connect(self, valve) -> bool:
        return valve in self.connects


valves: "dict[str: Valve]" = {}
distances: "dict['tuple[str, str]': int]" = {}
while inp := input():
    inp = inp.split(";")
    label, rate, connects = (
        inp[0][6:8],
        int(inp[0].split("=")[1]),
        (inp[1][(24 if inp[1].startswith(" tunnels") else 23) :]).split(", "),
    )
    valves[label] = Valve(label, rate, connects)


def get_shortest_distance(l1, l2):
    if valves[l1].does_connect(l2):
        return 1
    checks = valves[l1].connects[:]
    steps = defaultdict(lambda: 10000000)
    reached = 0
    for v in checks:
        steps[v] = 1
    while len(checks):
        cur = checks.pop()
        for nex in valves[cur].connects:
            if (steps[cur] + 1 < steps[nex]) and (nex != l1):
                steps[nex] = steps[cur] + 1
                if nex == l2:
                    reached = steps[nex]
                    continue
                checks.append(nex)
    return reached


meaningful_valves = {l for l in valves if valves[l].flow_rate > 0 or l == "AA"}
for l1 in meaningful_valves:
    for l2 in meaningful_valves - {"AA"}:
        if l1 == l2:
            continue
        distances[l1, l2] = get_shortest_distance(l1, l2)

possible_subsets = defaultdict(int)


def calculate_best_flow(cur="AA", time=26, flow=0, opened=set()):
    opened = opened | {cur}
    can_open = meaningful_valves - opened

    subset_to_check = tuple(opened - {"AA"})
    possible_subsets[subset_to_check] = max(possible_subsets[subset_to_check], flow)

    best_flow = 0
    for to_open in can_open:
        remaining_time = time - distances[cur, to_open] - 1
        if remaining_time > 0:
            total_flow = valves[to_open].flow_rate * remaining_time
            total_flow += calculate_best_flow(
                to_open, remaining_time, total_flow + flow, opened
            )
            if total_flow > best_flow:
                best_flow = total_flow
    return best_flow


calculate_best_flow()

# time can run out before checking all valves
# so take the best flow score of the next max no. of valves visited
def fill(cur=tuple(meaningful_valves - {"AA"})):
    if cur not in possible_subsets:
        best_flow = 0
        for v in cur:
            new_flow = fill(tuple(set(cur) - {v}))
            if new_flow > best_flow:
                best_flow = new_flow
        possible_subsets[cur] = best_flow
    return possible_subsets[cur]


fill()

best_flow = 0
for human_work in list(possible_subsets.keys()):
    elephant_work = tuple(meaningful_valves - {"AA"} - set(human_work))
    total_flow = possible_subsets[human_work] + possible_subsets[elephant_work]
    if total_flow > best_flow:
        best_flow = total_flow

print(best_flow)
