from collections import defaultdict

inp = 312051

grid = defaultdict(lambda: defaultdict(int))
grid[0][0] = 1

N = 10
x = y = 0
dx = 0
dy = -1
for i in range(N ** 2):
    if -N/2 < x <= N/2 and -N/2 < y <= N/2:
        for ddy in [-1, 0, 1]:
            for ddx in [-1, 0, 1]:
                if ddy == ddx == 0:
                    continue
                grid[y][x] += grid[y+ddy][x+ddx]

                if grid[y][x] >= inp:
                    print(grid[y][x])
                    exit()
    if x == y or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
        dx, dy = -dy, dx
    x, y = x + dx, y + dy
