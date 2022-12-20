og = []

i = 0
while inp := input():
    og.append((i, int(inp)))
    i += 1

for x in og[:]:
    id = og.index(x)
    og.pop(id)
    og.insert((id + x[1]) % len(og), x)

newg = [x for _, x in og]
ans = 0
for pos in (1000, 2000, 3000):
    ans += newg[(newg.index(0)+pos) % len(newg)]

print(ans)
