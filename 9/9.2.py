from itertools import combinations

goal = 70639851

with open("input", "r") as f:
    numbers = f.read().splitlines()

numbers = list(map(int, numbers))
size = 2
found = False

while not found:
    for a in range(len(numbers) - size + 2):
        b = a + size
        block = numbers[a:b]
        if sum(block) == goal:
            print(min(block) + max(block))
            found = True
    size += 1