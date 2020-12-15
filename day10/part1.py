
with open("input.txt") as f:
    lens = list(map(int, f.read().strip().split(",")))

ind = 0
skip = 0
rlind = 0
lst = [i for i in range(256)]


for l in lens:
    rev = lst[:l][::-1] + (lst[-(len(lst) - l):] if l < len(lst) else [])
    ind = (l + skip) % len(lst)
    rlind += (l + skip)
    rlind %= len(lst)
    if ind != 0:
        lst = rev[ind:] + rev[:ind]
    else:
        lst = rev
    skip += 1

lst = lst[-rlind:] + lst[:-rlind]
print(lst[0] * lst[1])
