
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

seen = set()
while True:
    ind = maxind(bs)
    r = bs[ind]
    bs[ind] = 0
    for i in range(1, r+1):
        bs[(ind+i) % len(bs)] += 1

    if tuple(bs) in seen:
        print(len(seen)+1)
        exit()
    seen.add(tuple(bs))
