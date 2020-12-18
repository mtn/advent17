import re

pp = []
vv = []
aa = []
with open("input.txt") as f:
    for i, line in enumerate(f):
        p, v, a = line.strip().split(", ")
        pp.append(list(map(int,re.findall("\d+",p))))
        vv.append(list(map(int,re.findall("\d+",v))))
        aa.append(list(map(int,re.findall("\d+",a))))

for s in range(100):
    for i in range(len(pp)):
        for j in range(3):
            vv[i][j] += aa[i][j]
        for j in range(3):
            pp[i][j] += vv[i][j]

def d(pt):
    return sum(abs(x) for x in pt)

min_pt = None
min_dst = 1e8
for i, p in enumerate(pp):
    if d(p) < min_dst:
        min_pt = i
        min_dst = d(p)
print(min_pt)
