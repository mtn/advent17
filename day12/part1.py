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

visited = set()
q = deque([0])
while q:
    n = q.popleft()
    if n in visited:
        continue
    visited.add(n)
    q.extend(g[n])
print(len(visited))
