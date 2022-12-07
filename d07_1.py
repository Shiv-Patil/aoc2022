files = {}
dirs = {"/": []}
cwd = []
input()
inp = input()
while True:
    if inp.startswith("$"):
        # command
        line = inp.split()
        cmd = line[1]
        if cmd == "cd":
            arg = line[2]
            if arg == "..":
                cwd.pop()
            else:
                cwd.append(arg)
                direc = f"/{'/'.join(cwd)}"
                if not dirs.get(direc):
                    dirs[direc] = []
            inp = input()
        elif cmd == "ls":
            while inp := input():
                if inp.startswith("$"):
                    break
                if not inp.startswith("dir"):
                    size, filename = inp.split()
                    filepath = f"/{'/'.join(cwd)}/{filename}" if cwd else f"/{filename}"
                    files[filepath] = int(size)
                    dirs[f"/{'/'.join(cwd)}"].append(filepath)
                else:
                    dirname = inp.split()[1]
                    dirpath = f"/{'/'.join(cwd)}/{dirname}/" if cwd else f"/{dirname}/"
                    dirs[f"/{'/'.join(cwd)}"].append(dirpath)
    if not inp:
        break

dirtotals = {}
dirpaths = list(dirs.keys())
dirpaths.sort(key=lambda x: len(x), reverse=True)

for dirpath in dirpaths:
    dirtotal = 0
    for child in dirs.get(dirpath):
        if not child.endswith("/"):
            dirtotal += files.get(child, 0)
        else:
            dirtotal += dirtotals.get(child[:-1])
    dirtotals[dirpath] = dirtotal

total = 0
for dirsize in dirtotals.values():
    if dirsize <= 100000:
        total += dirsize
print(total)
