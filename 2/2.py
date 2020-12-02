import re

with open("input", "r") as f:
    lines = f.read().splitlines()

valid1 = 0
valid2 = 0

for line in lines:
    regex = re.search(r"^(\d+)-(\d+) (.): (.*)$", line)
    a, b, letter, password = regex.groups()
    a, b = map(int, (a, b))
    if a <= password.count(letter) <= b:
        valid1 += 1
    if (password[a-1] == letter) ^ (password[b-1] == letter):
        valid2 += 1 

print(valid1, valid2)