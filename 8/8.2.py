
def loop(instructions, index):
    instructions = [[instruction, 0] for instruction in instructions]
    acc = 0
    cur = 0

    while True:

        try:
            instruction = instructions[cur][0]
        except IndexError:
            print(f"{index} : se termine, {acc=}")
            return

        instructions[cur][1] += 1

        if instructions[cur][1] == 2:
            print(f"{index} : boucle infinie.")
            return

        operator, operand = instruction.split(" ")
        operand = int(operand)

        if operator == "acc":
            acc += operand
            cur += 1
            continue
        elif operator == "jmp":
            cur += operand
            continue
        elif operator == "nop":
            cur += 1

if __name__ == "__main__":
    with open("input", "r") as f:
        instructions = f.read().splitlines()

    for i in range(len(instructions)):
        output = []

        nop_or_jmp = -1
        for instruction in instructions:
            operator, operand = instruction.split(" ")
            if operator in ("nop", "jmp"):
                nop_or_jmp += 1
                if nop_or_jmp == i:
                    operator = {"nop":"jmp", "jmp":"nop"}[operator]
            output.append(f"{operator} {operand}")
        loop(output, i)