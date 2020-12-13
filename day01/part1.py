
with open("input.txt") as f:
    ans = 0
    c = f.read().strip()

for c1, c2 in zip(c, c[1:]):
    if c1 == c2:
        ans += int(c1)
if c[-1] == c[0]:
    ans += int(c[0])

print(ans)
