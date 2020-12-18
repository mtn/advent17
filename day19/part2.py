
g = {}
with open("input.txt") as f:
    lines = f.read().rstrip().split("\n")

letters = {c for l in lines for c in l if c.isalpha()}
reached = []

for y, line in enumerate(lines):
    for x, cc in enumerate(line):
        if cc != " ":
            g[(x,y)] = cc

x = lines[0].index("|")
y = 0

dx = 0
dy = 1

ccw = [(1,0), (0,-1), (-1,0), (0,1)]
def left(dx, dy):
    ind = ccw.index((dx,dy))
    return ccw[(ind+1)%4]
def right(dx,dy):
    ind = ccw.index((dx,dy))
    return ccw[(ind-1)%4]

steps = 0
while len(reached) != len(letters):
    steps += 1
    if g[(x,y)] in letters:
        reached.append(g[(x,y)])
        if len(reached) == len(letters):
            print(steps)
            break

    if (x+dx, y+dy) in g:
        x = x+dx
        y = y+dy
        continue

    ldx, ldy = left(dx,dy)
    if (x+ldx, y+ldy) in g:
        dx = ldx
        dy = ldy
        x = x + dx
        y = y + dy
        continue

    rdx, rdy = right(dx,dy)
    assert (x+rdx, y+rdy) in g
    dx = rdx
    dy = rdy
    x = x + dx
    y = y + dy
