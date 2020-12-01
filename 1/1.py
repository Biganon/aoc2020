from itertools import combinations
from math import prod

with open("input", "r") as f:
    lines = f.read().splitlines()

numbers = map(int, lines)

repetitions = 3

pairs = combinations(numbers, repetitions)

correct_sum = next(pair for pair in pairs if sum(pair) == 2020)

print(prod(correct_sum))