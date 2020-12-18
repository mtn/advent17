from collections import defaultdict
import re

pp = {}
vv = {}
aa = {}
with open("input.txt") as f:
    for i, line in enumerate(f):
        p, v, a = line.strip().split(", ")
        pp[i] = list(map(int,re.findall("-?\d+",p)))
        vv[i] = list(map(int,re.findall("-?\d+",v)))
        aa[i] = list(map(int,re.findall("-?\d+",a)))

for s in range(100):
    locs = defaultdict(list)
    for i in pp:
        for j in range(3):
            vv[i][j] += aa[i][j]
        for j in range(3):
            pp[i][j] += vv[i][j]
        locs[tuple(pp[i])].append(i)

    for loc, pts in locs.items():
        if len(pts) > 1:
            for i in pts:
                del pp[i]
                del vv[i]
                del aa[i]

print(len(pp))
