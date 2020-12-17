import numpy as np
from copy import deepcopy

def pprint(grid):
    for z, slice_ in enumerate(grid):
        print(f"{z=}")
        for y, row in enumerate(slice_):
            line = "".join(map(str, map(int, row)))
            line = line.replace("0", ".").replace("1", "#")
            print(line)

with open("input", "r") as f:
    init = f.read().splitlines()

init2 = np.zeros((8, 8))
for y, row in enumerate(init):
    for x, cell in enumerate(row):
        if cell == "#":
            init2[y][x] = 1
        else:
            init2[y][x] = 0

grid = np.zeros((24, 24, 24))


for y, row in enumerate(init2):
    for x, cell in enumerate(row):
        grid[12][8+y][8+x] = cell

def iterate(grid):
    new = deepcopy(grid)
    for z, slice_ in enumerate(grid):
        for y, row in enumerate(slice_):
            for x, cell in enumerate(row):
                # print(f"{x} {y} {z}")
                n = 0
                for dz in range(-1, 2):
                    for dy in range(-1, 2):
                        for dx in range(-1, 2):
                            if dx == dy == dz == 0:
                                continue
                            try:
                                n += grid[z+dz][y+dy][x+dx]
                            except IndexError:
                                pass
                if cell == 1 and n not in (2, 3):
                    new[z][y][x] = 0
                elif cell == 0 and n == 3:
                    new[z][y][x] = 1
                else:
                    new[z][y][x] = cell
    return new

for i in range(6):
    grid = deepcopy(iterate(grid))

total = 0
for slice_ in grid:
    for row in slice_:
        for cell in row:
            total += cell
print(total)