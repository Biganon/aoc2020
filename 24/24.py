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

for i in range(100):

    to_test = dict((k,v) for (k,v) in tiles.items() if v)

    extras = {}
    for (x,y) in to_test.keys():
        for delta in deltas.values():
            dx, dy = delta.values()
            if dx == 0 and dy == 0:
                continue
            if (x+dx, y+dy) in to_test:
                continue
            if (x+dx) % 2 != (y+dy) % 2:
                continue
            extras[(x+dx, y+dy)] = False
    to_test.update(extras)

    new = defaultdict(lambda: False)

    for ((x,y), current) in to_test.items():
        nw = int(to_test.get((x-1, y+1), False))
        ne = int(to_test.get((x+1, y+1), False)) 
        sw = int(to_test.get((x-1, y-1), False)) 
        se = int(to_test.get((x+1, y-1), False)) 
        w  = int(to_test.get((x-2, y+0), False)) 
        e  = int(to_test.get((x+2, y+0), False)) 
        
        n = sum([nw, ne, sw, se, w, e])

        if current and (n == 0 or n > 2):
            pass
        elif not current and n == 2:
            new[(x, y)] = True
        elif current:
            new[(x, y)] = True

    print(f"Day {i+1}: {len([tile for tile in new.values() if tile])}")

    tiles = new