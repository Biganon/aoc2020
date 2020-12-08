with open("input", "r") as f:
    instructions = f.read().splitlines()

instructions = [[instruction, 0] for instruction in instructions]

acc = 0
cur = 0

while True:
    print(acc)
    instruction = instructions[cur][0]
    iterations = instructions[cur][1]
    if iterations == 0:
        pass
    else:
        print(acc)
        break

    instructions[cur][1] += 1

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