from collections import defaultdict

regs = defaultdict(int)

with open("input.txt") as f:
    for line in f:
        splt = line.strip().split()

        tgt = splt[0]
        instr = splt[1]
        if instr == "inc":
            val = int(splt[2])
        else:
            val = -int(splt[2])
        condreg = splt[4]
        cond = splt[5]
        condval = int(splt[6])

        exp = f"regs[\"{condreg}\"] {cond} {condval}"
        if eval(exp):
            regs[tgt] += val

print(max(regs.values()))

