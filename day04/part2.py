from collections import Counter
from itertools import combinations

def ana(w1, w2):
    c1 = Counter(w1)
    c2 = Counter(w2)

    return c1 == c2

nvalid = 0
with open("input.txt") as f:
    for line in f:
        words = line.strip().split()

        valid = True
        for w1, w2 in combinations(words, 2):
            valid = valid and not ana(w1, w2)
        nvalid += valid

print(nvalid)

