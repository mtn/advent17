from collections import defaultdict

def val(v):
    try:
        return int(v)
    except:
        return reg[v]

sounds = []
reg = defaultdict(int)
with open("input.txt") as f:
    lines = f.read().strip().split("\n")

ind = 0
while True:
    if ind < 0 or ind >= len(lines):
        break
    line = lines[ind]

    splt = line.strip().split()

    if line.startswith("snd"):
        sounds.append(reg[splt[1]])
    elif line.startswith("set"):
        reg[splt[1]] = val(splt[2])
    elif line.startswith("add"):
        reg[splt[1]] += val(splt[2])
    elif line.startswith("mul"):
        reg[splt[1]] *= val(splt[2])
    elif line.startswith("mod"):
        reg[splt[1]] %= val(splt[2])
    elif line.startswith("rcv"):
        if val(splt[1]) != 0:
            print(sounds[-1])
            exit()

    if line.startswith("jgz"):
        if val(splt[1]) > 0:
            ind += val(splt[2])
            continue

    ind += 1
