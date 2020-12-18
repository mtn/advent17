from collections import defaultdict

def val(v):
    try:
        return int(v)
    except:
        return reg[v]

reg = defaultdict(int)
with open("input.txt") as f:
    lines = f.read().strip().split("\n")

ind = 0
ans = 0
while True:
    if ind < 0 or ind >= len(lines):
        break
    line = lines[ind]

    splt = line.strip().split()

    if line.startswith("set"):
        reg[splt[1]] = val(splt[2])
    elif line.startswith("sub"):
        reg[splt[1]] -= val(splt[2])
    elif line.startswith("mul"):
        reg[splt[1]] *= val(splt[2])
        ans += 1
    elif line.startswith("mod"):
        reg[splt[1]] %= val(splt[2])
    if line.startswith("jnz"):
        if val(splt[1]) != 0:
            ind += val(splt[2])
            continue

    ind += 1

print(ans)
