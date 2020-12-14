import re
from itertools import combinations

with open("input", "r") as f:
    instructions = f.read().splitlines()

def get_memory_addresses(number, bitmask):
    output = []
    binary = list(f"{number:b}".rjust(36, "0"))
    for idx, bit in enumerate(bitmask):
        if bit == "0":
            continue
        else:
            binary[idx] = bit

    xs = [r.start() for r in re.finditer(r"X", "".join(binary))]
    combis = []
    for i in range(len(xs)+1):
        combis.extend(list(combinations(xs, i)))

    for combi in combis:
        copy = binary[::1]
        for idx, char in enumerate(copy):
            if idx in combi:
                copy[idx] = "1"
        output.append(int("".join(copy).replace("X", "0"), 2))

    return output

bitmask = None
memory = {}

for instruction in instructions:
    operation, value = instruction.split(" = ")
    if operation == "mask":
        bitmask = value
    else:
        address = int(operation[4:-1])

        addresses = get_memory_addresses(address, bitmask)
        for add in addresses:
            memory[add] = int(value)

print(sum(memory.values()))