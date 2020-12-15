

with open("input.txt") as f:
    lens = list(map(ord, f.read().strip()))
lens.extend([17, 31, 73, 47, 23])

ind = 0
skip = 0
rlind = 0
lst = [i for i in range(256)]


for i in range(64):
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

hxs = []
for i in range(256 // 16):
    nums = lst[i*16:(i+1)*16]
    dhsh = 0
    for n in nums:
        dhsh ^= n
    hxs.append(hex(dhsh)[2:].zfill(2))

print("".join(hxs))
