from collections import defaultdict, deque

def val(v):
    try:
        return int(v)
    except:
        return reg[v]

sounds = []
with open("input.txt") as f:
    lines = f.read().strip().split("\n")

indA = indB = 0
regA = defaultdict(int)
regB = defaultdict(int)
regA["p"] = 0
regB["p"] = 1
qA = deque()
qB = deque()
rA = True
blocked = [False, False]
ans = 0
while True:
    if all(blocked):
        break
    rA = not blocked[0]

    reg = regA if rA else regB
    myq, otherq = (qA,qB) if rA else (qB,qA)
    ind = indA if rA else indB

    if ind < 0 or ind >= len(lines):
        break
    line = lines[ind]

    splt = line.strip().split()

    if line.startswith("snd"):
        v = val(splt[1])
        if rA:
            blocked[1] = False
        else:
            blocked[0] = False
            ans += 1
        otherq.append(v)
    elif line.startswith("set"):
        reg[splt[1]] = val(splt[2])
    elif line.startswith("add"):
        reg[splt[1]] += val(splt[2])
    elif line.startswith("mul"):
        reg[splt[1]] *= val(splt[2])
    elif line.startswith("mod"):
        reg[splt[1]] %= val(splt[2])
    elif line.startswith("rcv"):
        if not myq:
            if rA:
                blocked[0] = True
            else:
                blocked[1] = True
            continue
        reg[splt[1]] = myq.popleft()
    if line.startswith("jgz"):
        if val(splt[1]) > 0:
            ind += val(splt[2])
            if rA:
                indA = ind
            else:
                indB = ind
            continue

    ind += 1

    if rA:
        indA = ind
    else:
        indB = ind

print(ans)
