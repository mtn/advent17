from collections import defaultdict, deque
from copy import deepcopy

comps = defaultdict(set)
with open("input.txt") as f:
    for line in f:
        l,r = map(int, line.strip().split("/"))
        comps[l].add(r)
        comps[r].add(l)

def strength(bridge):
    tot = 0
    for x,y in bridge:
        tot += x + y
    return tot

strongest = 0
q = deque([(x, [(0,x)]) for x in comps[0]])
while q:
    at, bridge = q.popleft()

    possible = comps[at]
    available = []
    for o in possible:
        if (at, o) in bridge or (o, at) in bridge:
            continue
        available.append((at, o))
        nb = deepcopy(bridge)
        nb.append((at, o))
        q.append((o, nb))

    if not available:
        strongest = max(strongest, strength(bridge))
        continue

print(strongest)
