from math import prod

with open("input", "r") as f:
    grid = f.read().splitlines()

def collisions(dx, dy):
    row = 0
    column = 0

    trees = 0

    while True:
        try:
            position = grid[row][column]
        except IndexError:
            return trees
        if position == "#":
            trees += 1
        row += dy
        column += dx
        column %= len(grid[0])

slopes = ((1,1), (3,1), (5,1), (7,1), (1,2))

print(prod(collisions(*slope) for slope in slopes))