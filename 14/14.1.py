with open("input", "r") as f:
    instructions = f.read().splitlines()

def apply_bitmask(number, bitmask):
    binary = list(f"{number:b}".rjust(36, "0"))
    for idx, bit in enumerate(bitmask):
        if bit == "X":
            continue
        binary[idx] = bit
    return int("".join(binary), 2)

bitmask = None
memory = {}

for instruction in instructions:
    operation, value = instruction.split(" = ")
    if operation == "mask":
        bitmask = value
    else:
        address = int(operation[4:-1])
        memory[address] = apply_bitmask(int(value), bitmask)

print(sum(memory.values()))