from collections import deque

inp = "oundnydw"


def kh(lens):
    lens = lens + [17, 31, 73, 47, 23]
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

    return "".join(hxs)

def used(n):
    us = [0] * 4
    i = 3
    while n:
        us[i] = bool(1 & n)
        n >>= 1
        i -= 1
    return us

ans = 0
for i in range(128):
    k = kh(list(map(ord, f"{inp}-{i}")))
    row = []
    for c in k:
        ans += sum(used(int(c, 16)))

print(ans)
