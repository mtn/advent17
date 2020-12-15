from collections import deque

steps = 356

d = deque([0])

pos = 0
for i in range(1, 2018):
    d.rotate(-steps-1)
    d.appendleft(i)

for d1, d2 in zip(d, list(d)[1:]):
    if d1 == 2017:
        print(d2)
        exit()
