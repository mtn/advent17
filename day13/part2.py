
rngs = {}
with open("input.txt") as f:
    for line in f:
        layer, rng = map(int, line.strip().split(": "))
        rngs[layer] = rng

t = 0
while True:
    good = True
    for dpth, rng in rngs.items():
        pos = (dpth + t) % (2 * (rng - 1))
        if pos >= rng:
            pos = rng - 1 - pos%rng

        if pos == 0:
            good = False

    if good:
        print(t)
        exit()

    t += 1
