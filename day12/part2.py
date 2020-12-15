from collections import defaultdict, deque

g = defaultdict(list)
with open("input.txt") as f:
    for line in f:
        inpipe, outpipes = line.split(" <-> ")
        inpipe = int(inpipe)
        outpipes = list(map(int, outpipes.split(", ")))

        g[inpipe].extend(outpipes)
        for o in outpipes:
            g[o].append(inpipe)

unvisited = set(g.keys())
visited = set()
groups = 0
while unvisited:
    start = list(unvisited)[0]
    groups += 1
    q = deque([start])
    while q:
        n = q.popleft()
        if n in visited:
            continue
        visited.add(n)
        unvisited.remove(n)
        q.extend(g[n])

print(groups)
