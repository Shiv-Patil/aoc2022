overlaps = 0
while inp := input():
    first, second = map(lambda x: (*map(int, x.split("-")),), inp.split(","))
    if (
        (first[0] >= second[0] and first[0] <= second[1])
        or (first[1] >= second[0] and first[1] <= second[1])
        or (second[0] >= first[0] and second[0] <= first[1])
        or (second[1] >= first[0] and second[1] <= first[1])
    ):
        overlaps += 1
print(overlaps)
