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

grid = []
for i in range(128):
    k = kh(list(map(ord, f"{inp}-{i}")))
    row = []
    for c in k:
        u = used(int(c, 16))
        row.extend(u)
    grid.append(row)

groups = 0
unchecked = set((y, x) for x in range(128) for y in range(128) if grid[y][x])
while unchecked:
    groups += 1
    start = list(unchecked)[0]
    q = deque([start])
    while q:
        y, x = q.popleft()
        if (y, x) not in unchecked:
            continue
        unchecked.remove((y, x))
        for (dy, dx) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if x + dx < 0 or x + dx >= len(grid[0]) or y + dy < 0 or y + dy >= len(grid):
                continue
            if (y+dy, x+dx) not in unchecked:
                continue
            if not grid[y+dy][x+dx]:
                unchecked.remove((y+dy, x+dx))
            q.append((y+dy, x+dx))

print(groups)
