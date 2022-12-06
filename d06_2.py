inp = input()
n = 14
for i in range(0, len(inp)-n-1):
    chars = inp[i:i+n]
    if len(set(chars)) == n:
        print(i+n)
        break
