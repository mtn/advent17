from itertools import combinations

cs = 0
with open("input.txt") as f:
    for line in f:
        nums = list(map(int, line.strip().split()))
        cs += max(nums) - min(nums)

print(cs)
