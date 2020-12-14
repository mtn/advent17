
with open("input.txt") as f:
    bs = list(map(int, f.read().strip().split()))

def maxind(l):
    mxv = l[0]
    mxind = 0
    for i, v in enumerate(l):
        if v > mxv:
            mxv = v
            mxind = i
    return mxind

seen = {tuple(bs): 0}
while True:
    ind = maxind(bs)
    r = bs[ind]
    bs[ind] = 0
    for i in range(1, r+1):
        bs[(ind+i) % len(bs)] += 1

    bst = tuple(bs)
    if bst in seen:
        print(len(seen) - seen[bst])
        exit()

    seen[bst] = len(seen)
