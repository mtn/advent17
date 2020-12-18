from collections import defaultdict

g = defaultdict(bool)
with open("input.txt") as f:
    c = f.read().strip().split("\n")
    for y,row in enumerate(c):
        for x, cc in enumerate(row):
            g[(x,y)] = cc == "#"

dirs = [(0,-1), (-1,0), (0,1), (1,0)]
def left(dx,dy):
    ind = dirs.index((dx,dy))
    return dirs[(ind+1)%4]

def right(dx,dy):
    ind = dirs.index((dx,dy))
    return dirs[(ind-1)%4]

nrows = len(c)
ncols = len(c[0])
dx,dy = 0,-1
x,y = ncols//2, nrows//2

ans = 0
for i in range(10000):
    if g[(x,y)]:
        dx,dy = right(dx,dy)
    else:
        dx,dy = left(dx,dy)
    g[(x,y)] = not g[(x,y)]
    ans += g[(x,y)]
    x += dx
    y += dy

def pgrid(g):
    xs = [x[0] for x in g.keys()]
    ys = [x[1] for x in g.keys()]

    for y in range(min(ys), max(ys)+1):
        print("".join(g[(x,y)] if (x,y) in g else '.' for x in range(min(xs), max(xs)+1)))


print(ans)


