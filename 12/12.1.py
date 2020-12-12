from collections import deque

position_deltas = {"N":{"X":0,"Y":1}, "E":{"X":1,"Y":0}, "S":{"X":0,"Y":-1}, "W":{"X":-1,"Y":0}}
orientation_deltas = {"R":-1, "L":1} # deque.rotate() is "inverted", -1 goes forward, 1 goes backwards
orientations = deque(["E", "S", "W", "N"])

with open("input", "r") as f:
    instructions = f.read().splitlines()

position = {"X":0,"Y":0}

for instruction in instructions:
    operation = instruction[0]
    value = int(instruction[1:])
    if operation in position_deltas.keys():
        position["X"] += position_deltas[operation]["X"] * value
        position["Y"] += position_deltas[operation]["Y"] * value
    elif operation in orientation_deltas.keys():
        orientations.rotate((value // 90) * orientation_deltas[operation])
    else:
        position["X"] += position_deltas[orientations[0]]["X"] * value
        position["Y"] += position_deltas[orientations[0]]["Y"] * value
    print(position, orientations[0])

print(sum(map(abs, position.values())))