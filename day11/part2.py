
x = y = 0
with open("input.txt") as f:
    c = f.read().strip()
dirs = c.split(",")
dsts = set()

def dst(x, y):
    return abs(x) + (abs(y) - abs(x)) // 2

for d in dirs:
    dsts.add(dst(x, y))
    if d == "n":
        y -= 2
    elif d == "s":
        y += 2
    elif d == "nw":
        y -= 1
        x -= 1
    elif d == "ne":
        y -= 1
        x += 1
    elif d == "se":
        y += 1
        x += 1
    elif d == "sw":
        y += 1
        x -= 1

print(max(dsts))
