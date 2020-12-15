orig = "abcdefghijklmnop"
ps = list(orig)
with open("input.txt") as f:
    instrs = f.read().strip().split(",")

seen = []
for i in range(1000000000):
    st = tuple(ps)
    if st in seen:
        print("".join(seen[1000000000 % len(seen)]))
        exit()
    seen.append(st)

    for i in instrs:
        if i.startswith("s"):
            sz = int(i[1:])
            if sz > 0:
                ps = ps[-sz:] + ps[:len(ps)-sz]
        elif i.startswith("x"):
            p1, p2 = map(int, i[1:].split("/"))
            tmp = ps[p1]
            ps[p1] = ps[p2]
            ps[p2] = tmp
        elif i.startswith("p"):
            l1, l2 = i[1:].split("/")
            p1, p2 = ps.index(l1), ps.index(l2)
            tmp = ps[p1]
            ps[p1] = ps[p2]
            ps[p2] = tmp
