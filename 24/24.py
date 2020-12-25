from collections import defaultdict
import re
from copy import deepcopy

tiles = defaultdict(lambda: False)

deltas = {"nw":{"x":-1, "y":+1},
          "ne":{"x":+1, "y":+1},
          "sw":{"x":-1, "y":-1},
          "se":{"x":+1, "y":-1},
          "w" :{"x":-2, "y":+0},
          "e" :{"x":+2, "y":+0}}

with open("input", "r") as f:
    lines = f.read().splitlines()

for line in lines:
    cursor = {"x":0, "y":0}
    moves = re.findall(r"(?:[ns]?e|[ns]?w)", line)
    for move in moves:
        delta = deltas[move]
        cursor["x"] += delta["x"]
        cursor["y"] += delta["y"]
    tuple_ = (cursor["x"], cursor["y"])
    tiles[tuple_] = not tiles[tuple_]

# print(len([tile for tile in tiles.values() if tile]))

###

for i in range(100):

    new = defaultdict(lambda: False)

    minx = min(tile[0] for tile in tiles)-2
    maxx = max(tile[0] for tile in tiles)+2
    miny = min(tile[1] for tile in tiles)-2
    maxy = max(tile[1] for tile in tiles)+2

    # print(f"{minx=} {maxx=} {miny=} {maxy=}")

    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            # print(f"Testing {x=} {y=}")
            current = len([k for k,v in tiles.items() if k[0] == x and k[1] == y and v])
            # print(f"{current=}")
            nw = len([k for k,v in tiles.items() if k[0] == x-1 and k[1] == y+1 and v])
            # print(f"{nw=}")
            ne = len([k for k,v in tiles.items() if k[0] == x+1 and k[1] == y+1 and v])
            # print(f"{ne=}")
            sw = len([k for k,v in tiles.items() if k[0] == x-1 and k[1] == y-1 and v])
            # print(f"{sw=}")
            se = len([k for k,v in tiles.items() if k[0] == x+1 and k[1] == y-1 and v])
            # print(f"{se=}")
            w  = len([k for k,v in tiles.items() if k[0] == x-2 and k[1] == y+0 and v])
            # print(f"{w=}")
            e  = len([k for k,v in tiles.items() if k[0] == x+2 and k[1] == y+0 and v])
            # print(f"{e=}")
            n = sum([nw, ne, sw, se, w, e])
            # print(f"{n=}")
            if current and (n == 0 or n > 2):
                pass
            elif not current and n == 2:
                new[(x, y)] = True
            elif current:
                new[(x, y)] = True

    print(f"Day {i+1}: {len([tile for tile in new.values() if tile])}")

    tiles = new