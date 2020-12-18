"""
b = 84
c = b
if (a != 0) GOTO A
GOTO B
A: b = b * 100 + 100000
c = b + 17000
B: f = 1
d = 2
E: e = 2
D: g = d * e - b
if (g != 0) GOTO C
f = 0
C: e += 1
g = e - b
if (g != 0) GOTO D
d += 1
g = d - b
if (g != 0) GOTO E
if (f != 0) GOTO F
h += 1
F: g = b
g -= c
if (g != 0) GOTO H
END
b += 17
GOTO B
"""

from collections import defaultdict

reg = defaultdict(int)
reg["b"] = 84 * 100 + 100000
reg["c"] = reg["b"] + 17000

while True:
    reg["f"] = 1
    reg["d"] = 2
    while reg["d"] < reg["b"]:
        if reg["b"] % reg["d"] == 0:
            reg["f"] = 0
            break
        reg["d"] += 1

    if reg["f"] == 0:
        reg["h"] += 1

    reg["g"] = reg["b"] - reg["c"]
    reg["b"] += 17

    if reg["g"] == 0:
        break

print(reg["h"])
