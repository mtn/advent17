
inp = 312051

n = 1
while inp > n ** 2:
    n += 2

mid = (n-2) ** 2 + 1 + (n // 2) - 1
while not abs(inp - mid) <= n // 2:
    mid += n - 1
print(abs(mid - inp) + n // 2)
