from itertools import combinations

with open("input", "r") as f:
    numbers = f.read().splitlines()

numbers = list(map(int, numbers))

while True:
    block = numbers[:25]
    sums = list(map(sum, combinations(block, 2)))
    if numbers[25] in sums:
        numbers.pop(0)
        continue
    else:
        print(numbers[25])
        break