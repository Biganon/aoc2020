from collections import deque

position_deltas = {"N":{"X":0,"Y":1}, "E":{"X":1,"Y":0}, "S":{"X":0,"Y":-1}, "W":{"X":-1,"Y":0}}
to_invert = {"R":"Y", "L":"X"} # what coordinate to invert, depending on the rotation direction

with open("input", "r") as f:
    instructions = f.read().splitlines()

waypoint = {"X":10,"Y":1}
boat = {"X":0, "Y":0}

print(f"{boat=}, {waypoint=}")
for instruction in instructions:
    operation = instruction[0]
    value = int(instruction[1:])
    if operation in position_deltas.keys():
        waypoint["X"] += position_deltas[operation]["X"] * value
        waypoint["Y"] += position_deltas[operation]["Y"] * value
    elif operation in to_invert.keys():
        for i in range(abs(value//90)):
            waypoint["X"], waypoint["Y"] = waypoint["Y"], waypoint["X"]
            waypoint[to_invert[operation]] *= -1
    else:
        for i in range(value):
            boat["X"] += waypoint["X"]
            boat["Y"] += waypoint["Y"]
    print(f"{boat=}, {waypoint=}")

print(sum(map(abs, boat.values())))