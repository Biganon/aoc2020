from copy import deepcopy

with open("input", "r") as f:
    grid = f.read().splitlines()

grid = list(map(list, grid))

while True:
    new = deepcopy(grid)
    print(sum(row.count("#") for row in grid))
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            neighbors = []
            for (dy, dx) in ((-1, -1), (-1, +0), (-1, +1),
                             (+0, -1), (+0, +1),
                             (+1, -1), (+1, +0), (+1, +1)):
                tx = x
                ty = y
                nearest = "."
                while 0 <= tx+dx <= len(grid[0])-1 and 0 <= ty+dy <= len(grid)-1:
                    tx += dx
                    ty += dy
                    nearest = grid[ty][tx]
                    if nearest != ".":
                        break
                neighbors.append(nearest)

            if grid[y][x] == "L" and neighbors.count("#") == 0:
                new[y][x] = "#"

            if grid[y][x] == "#" and neighbors.count("#") >= 5:
                new[y][x] = "L"

    grid = deepcopy(new)