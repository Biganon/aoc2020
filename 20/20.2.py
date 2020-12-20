from math import prod
from copy import deepcopy
import sys
import regex

with open("input", "r") as f:
    data = f.read()

class Tile:
    def __init__(self, id_, grid, borders, borders_set):
        self.id_ = id_
        self.grid = grid
        self.borders = borders
        self.borders_set = borders_set

        self.x = None
        self.y = None
        self.r = 0
        self.fx = 0
        self.fy = 0
        self.used = False
        self.locked = False

    def __str__(self):
        return f"{self.id_} [{self.x}-{self.y}]: {self.borders}"

    def __repr__(self):
        return f"<Tile ID {self.id_}>"

    def __eq__(self, other):
        return self.id_ == other.id_

    def __hash__(self):
        return hash(self.id_)

    def connections(self):
        output = []
        friends = [other for other in tiles.values() if other != self and self.borders_set & other.borders_set]
        for friend in friends:
            shared_borders = self.borders_set & friend.borders_set
            for shared_border in shared_borders:
                here = next(k for (k,v) in self.borders.items() if v == shared_border)
                there = next(k for (k,v) in friend.borders.items() if v == shared_border)
                output.append((here, self.id_, there, friend.id_))
        return output

    @property
    def mod_borders(self):
        output = deepcopy(self.grid)
        if self.fx:
            output = [row[::-1] for row in output]
        if self.fy:
            output = output[::-1]
        for i in range(self.r):
            output = list(zip(*output[::-1]))
        north = "".join(output[0])
        east = "".join([line[-1] for line in output])
        south = "".join(output[-1])
        west = "".join([line[0] for line in output])
        borders = {"n":north,
                   "e":east,
                   "s":south,
                   "w":west}
        return borders

def pprint(grid, ret=False):
    w = len(grid[0][0].grid[0])
    output = [["." for y in range(12*w)] for x in range(12*w)]
    for y, row in enumerate(grid):
        for x, tile in enumerate(row):
            if not tile:
                for py in range(w):
                    for px in range(w):
                        output[py+y*w][px+x*w] = "."
            else:                
                patch = deepcopy(tile.grid)
                if tile.fx:
                    patch = [row[::-1] for row in patch]
                if tile.fy:
                    patch = patch[::-1]
                for i in range(tile.r):
                    patch = list(zip(*patch[::-1]))
                for py, row in enumerate(patch):
                    for px, cell in enumerate(row):
                        output[py+y*w][px+x*w] = cell
    if not ret:
        for row in output:
            print("".join(row))
    else:
        return output

tiles_text = data.split("\n\n")
tiles_text = [t for t in tiles_text if t]
tiles = {}
for tile_text in tiles_text:
    lines = tile_text.splitlines()
    id_ = int(lines[0][5:9])
    grid = lines[1:]
    north = lines[1]
    east = "".join([line[-1] for line in lines[1:]])
    south = lines[-1][::-1]
    west = "".join([line[0] for line in lines[1:]])[::-1]
    borders = {"n":north,
               "e":east,
               "s":south,
               "w":west,
               "N":north[::-1],
               "E":east[::-1],
               "S":south[::-1],
               "W":west[::-1]}
    borders_set = set(borders.values())
    tile = Tile(id_=id_, grid=grid, borders=borders, borders_set=borders_set)
    tiles[id_] = tile

grid = [[None for y in range(12)] for x in range(12)]

tiles[1987].fy = 1
grid[0][0] = tiles[1987]
tiles[1987].used = True
tiles[1987].locked = True

tiles[1931].fy = 1
grid[1][0] = tiles[1931]
tiles[1931].used = True
tiles[1931].locked = True

y = -1
finished = False

while not finished:
    y += 1
    y %= 12
    for x in range(12):
        if grid[y][x]:
            continue
        neighbors = []
        for (dx, dy) in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if not (0 <= y+dy < 12 and 0 <= x+dx < 12):
                continue
            neighbor = grid[y+dy][x+dx]
            if neighbor:
                neighbors.append(neighbor)
        candidates = [set([x[3] for x in tile.connections()]) for tile in neighbors]
        try:
            common_candidates = set.intersection(*candidates)
        except TypeError:
            common_candidates = set()
        valid_candidates = [c for c in common_candidates if not tiles[c].used]
        if len(valid_candidates) == 1:
            grid[y][x] = tiles[valid_candidates[0]]
            tiles[valid_candidates[0]].used = True
        
        if len([t for t in tiles.values() if t.used]) == 12**2:
            finished = True

y = -1
finished = False

while not finished:
    y += 1
    y %= 12
    for x in range(12):
        tile = grid[y][x]
        if tile.locked:
            continue

        locked_neighbors = []
        for (dx, dy) in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if not (0 <= y+dy < 12 and 0 <= x+dx < 12):
                continue
            neighbor = grid[y+dy][x+dx]
            if neighbor and neighbor.locked:
                locked_neighbors.append((neighbor, (dx, dy)))

        for r in range(4):
            for fx in range(2):
                for fy in range(2):
                    if not tile.locked:
                        tile.r, tile.fx, tile.fy = r, fx, fy
                        for locked_neighbor in locked_neighbors:
                            ref, pos = locked_neighbor
                            dx, dy = pos
                            if dy == -1:
                                criteria = ref.mod_borders["s"]
                                tested = tile.mod_borders["n"]
                            elif dx == 1:
                                criteria = ref.mod_borders["w"]
                                tested = tile.mod_borders["e"]
                            elif dy == 1:
                                criteria = ref.mod_borders["n"]
                                tested = tile.mod_borders["s"]
                            elif dx == -1:
                                criteria = ref.mod_borders["e"]
                                tested = tile.mod_borders["w"]

                            if criteria == tested:
                                tile.locked = True
                                break
        if len([t for t in tiles.values() if t.locked]) == 12**2:
            finished = True

for tile in tiles.values():
    tile.grid = tile.grid[1:-1]
    tile.grid = [row[1:-1] for row in tile.grid]

original_atlas = pprint(grid, ret=True)

regex1 = r"..................#."
regex2 = r"#....##....##....###"
regex3 = r".#..#..#..#..#..#..."

idx1 = [idx for idx, c in enumerate(regex1) if c == "#"]
idx2 = [idx for idx, c in enumerate(regex2) if c == "#"]
idx3 = [idx for idx, c in enumerate(regex3) if c == "#"]

def find_monsters(atlas):
    monsters = []
    for idx, row in enumerate(atlas):
        if idx in (0, len(atlas)-1):
            continue
        r1 = set(r.start() for r in regex.finditer(regex1, "".join(atlas[idx-1]), overlapped=True))
        r2 = set(r.start() for r in regex.finditer(regex2, "".join(atlas[idx]), overlapped=True))
        r3 = set(r.start() for r in regex.finditer(regex3, "".join(atlas[idx+1]), overlapped=True))

        if i := set.intersection(r1, r2, r3):
            for m in i:
                monsters.append((idx-1, m))
    return monsters

finished = False
for r in range(4):
    if finished:
        break
    for fx in range(2):
        if finished:
            break
        for fy in range(2):
            if finished:
                break
            atlas = deepcopy(original_atlas)
            for i in range(r):
                atlas = list(zip(*atlas[::-1]))
            if fx:
                atlas = [row[::-1] for row in atlas]
            if fy:
                atlas = atlas[::-1]
            atlas_list = [list(row) for row in atlas]
            monsters = find_monsters(atlas)
            for monster in monsters:
                row, col = monster
                for idx in idx1:
                    atlas_list[row][col+idx] = "O"
                for idx in idx2:
                    atlas_list[row+1][col+idx] = "O"
                for idx in idx3:
                    atlas_list[row+2][col+idx] = "O"

            if monsters:
                roughness = 0
                for row in atlas_list:
                    roughness += row.count("#")

                print(roughness)
                finished = True