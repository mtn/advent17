
valid = 0
with open("input.txt") as f:
    for line in f:
        words = line.strip().split()
        uniq = set(words)
        valid += len(words) == len(uniq)

print(valid)

