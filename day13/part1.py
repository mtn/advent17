
rngs = {}
with open("input.txt") as f:
    for line in f:
        layer, rng = map(int, line.strip().split(": "))
        rngs[layer] = rng

s = 0

for dpth, rng in rngs.items():
    pos = dpth % (2 * (rng - 1))
    if pos >= rng:
        pos = rng - 1 - pos%rng
    if pos == 0:
        s += dpth * rng

print(s)
