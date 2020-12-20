from math import prod

with open("input", "r") as f:
    data = f.read()

tiles_text = data.split("\n\n")
tiles_text = [t for t in tiles_text if t]

class Tile:
    def __init__(self, id_, borders, borders_set):
        self.id_ = id_
        self.borders = borders
        self.borders_set = borders_set

        self.x = None
        self.y = None

    def __str__(self):
        return f"{self.id_} [{self.x}-{self.y}]: {self.borders}"

    def __eq__(self, other):
        return self.id_ == other.id_

    def __hash__(self):
        return hash(self.id_)

    def friends(self):
        return [other for other in tiles.values() if other != self and self.borders_set & other.borders_set]


tiles = {}

for tile_text in tiles_text:
    lines = tile_text.splitlines()
    id_ = int(lines[0][5:9])
    north = lines[1]
    east = "".join([line[-1] for line in lines[1:]])
    south = lines[-1]
    west = "".join([line[0] for line in lines[1:]])
    borders = {"n":north,
               "e":east,
               "s":south,
               "w":west,
               "N":north[::-1],
               "E":east[::-1],
               "S":south[::-1],
               "W":west[::-1]}
    borders_set = set(borders.values())
    tile = Tile(id_=id_, borders=borders, borders_set=borders_set)
    tiles[id_] = tile

corners = []

for idx, tile in enumerate(tiles.values()):
    friends = tile.friends()
    if len(friends) == 2:
        corners.append(tile.id_)

print(prod(corners))