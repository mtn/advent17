import numpy as np

def p2m(p):
    rows = p.split("/")
    m = np.array([[rr == "#" for rr in r] for r in rows])
    return m

def m2p(m):
    m = list(m)
    out= []
    for mm in m:
        out.append("".join(["#" if c else "." for c in mm]))
    return "/".join(out)

evenr = {}
oddr = {}
with open("input.txt") as f:
    for line in f:
        inp, out = line.strip().split(" => ")
        inp, out = p2m(inp), p2m(out)
        d = evenr if inp.shape[0] % 2 == 0 else oddr
        for k in range(4):
            r = np.rot90(inp, k=k)
            d[str(r)] = out
            d[str(np.flipud(r))] = out
            d[str(np.fliplr(r))] = out

s = p2m(".#./..#/###")
for _ in range(5):
    if s.shape[0] % 2 == 0:
        rows = []
        for i in range(s.shape[0]//2):
            cols = []
            for j in range(s.shape[0]//2):
                inm = s[2*i:2*(i+1), 2*j:2*(j+1)]
                ins = str(inm)
                out = evenr[ins]
                cols.append(out)
            row = np.hstack(cols)
            rows.append(row)
        s = np.vstack(rows)
        continue
    elif s.shape[0] % 3 == 0:
        rows = []
        for i in range(s.shape[0]//3):
            cols = []
            for j in range(s.shape[0]//3):
                inm = s[3*i:3*(i+1), 3*j:3*(j+1)]
                ins = str(inm)
                out = oddr[ins]
                cols.append(out)
            row = np.hstack(cols)
            rows.append(row)
        s = np.vstack(rows)
        continue

print(s.sum())
