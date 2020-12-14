
nums = []
with open("input.txt") as f:
    for line in f:
        nums.append(int(line.strip()))

ind = 0
steps = 0

while ind < len(nums):
    tmp = ind
    ind += nums[ind]
    nums[tmp] += 1
    steps += 1

print(steps)


