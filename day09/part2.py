

with open("input.txt") as f:
    c = f.read().strip()

depth = 0
ans = 0
in_garbage = False
next_invalid = False
for cc in c:
    if next_invalid:
        next_invalid = False
        continue
    if cc == "!":
        next_invalid = True
        continue
    if in_garbage:
        if cc == ">":
            in_garbage = False
            continue
        ans += 1
        continue

    if cc == "{":
        depth += 1
    elif cc == "}" and depth >= 0:
        depth -= 1
    elif cc == "<":
        in_garbage = True

print(ans)
