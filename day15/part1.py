
gaf = 16807
gbf = 48271
divf = 2147483647

ga = 618
gb = 814

mask = 0
for i in range(16):
    mask += 2 ** i

ans = 0
for i in range(int(4e7)):
    ga = (ga*gaf) % divf
    gb = (gb*gbf) % divf

    ans += (ga&mask) == (gb&mask)

print(ans)


