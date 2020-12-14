from collections import Counter

base = "mkxke"

towers = {}
weights = {}
with open("input.txt") as f:
    for line in f:
        splt = line.strip().split()
        name = splt[0]
        weights[name] = int(splt[1][1:-1])

        if "->" in line:
            ind = line.index("-")
            towers[name] = under = line[ind+2:].strip().split(", ")

def stw(n):
    if n not in towers:
        return weights[n]

    return weights[n] + sum(stw(nn) for nn in towers[n])

stws = {}
for n in weights.keys():
    stws[n] = stw(n)

def fnd(n, d):
    stwb = Counter(stws[n] for n in towers[n])
    if len(stwb) == 1:
        return n, weights[n] + d

    (w1, _), (w2, _) = stwb.most_common(2)
    for nn in towers[n]:
        if stws[nn] == w2:
            return fnd(nn, w1 - w2)

print(fnd(base, 0)[1])
