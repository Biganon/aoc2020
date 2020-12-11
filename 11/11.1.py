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
                if 0 <= x+dx <= len(grid[0])-1 and 0 <= y+dy <= len(grid)-1: 
                    neighbor = grid[y+dy][x+dx]
                else:
                    neighbor = "."
                neighbors.append(neighbor)

            if grid[y][x] == "L" and neighbors.count("#") == 0:
                new[y][x] = "#"

            if grid[y][x] == "#" and neighbors.count("#") >= 4:
                new[y][x] = "L"
    grid = deepcopy(new)