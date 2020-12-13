from itertools import combinations

cs = 0
with open("input.txt") as f:
    for line in f:
        nums = list(map(int, line.strip().split()))

        for n1, n2 in combinations(nums, 2):
            mn, mx = min(n1, n2), max(n1, n2)
            if mx % mn == 0:
                cs += mx // mn

print(cs)
