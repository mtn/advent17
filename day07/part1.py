
ns = set()
notit = set()
with open("input.txt") as f:
    for line in f:
        splt = line.strip().split()
        name = splt[0]
        ns.add(name)
        if "->" in line:
            ind = line.index("-")
            unders = line[ind+2:].strip().split(", ")
            for u in unders:
                notit.add(u)

print(list(ns - notit)[0])
