
with open("input.txt") as f:
    ans = 0
    c = f.read().strip()

ans = 0
for i, cc in enumerate(c):
    ind = (i + len(c) // 2) % len(c)
    if cc == c[ind]:
        ans += int(cc)

print(ans)

