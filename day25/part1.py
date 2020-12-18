from collections import defaultdict
import re

with open("input.txt") as f:
    sections = f.read().strip().split("\n\n")

nsteps = int(re.findall("\d+", sections[0].split("\n")[1])[0])

states = {}
for s in sections[1:]:
    lines = s.strip().split("\n")
    state = lines[0][-2]
    zwv = int(re.findall("\d", lines[2])[0])
    owv = int(re.findall("\d", lines[6])[0])
    znm = "l" if "left" in lines[3] else "r"
    onm = "l" if "left" in lines[7] else "r"
    zns = lines[4].strip()[-2]
    ons = lines[8].strip()[-2]

    states[state] = {"zwv":zwv,"owv":owv,"znm":znm,"onm":onm,"zns":zns,"ons":ons}

tape = defaultdict(int)
ind = 0
state = "A"
for _ in range(nsteps):
    info = states[state]
    if tape[ind] == 0:
        tape[ind] = info["zwv"]
        nm = info["znm"]
        state = info["zns"]
    else:
        tape[ind] = info["owv"]
        nm = info["onm"]
        state = info["ons"]

    if nm == "l":
        ind -= 1
    else:
        ind += 1

print(sum(tape.values()))

