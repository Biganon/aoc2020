import re

with open("input", "r") as f:
    lines = f.read().splitlines()

def treat_par(par):
    if par[0] == "(":
        par = par[1:]
    if par[-1] == ")":
        par = par[:-1]
    things = par.split()
    total = int(things[0])
    for i in range(1, len(things)-1, 2):
        operator = things[i]
        value = int(things[i+1])
        if operator == "+":
            total += value
        elif operator == "*":
            total *= value
    return str(total)

grand_total = 0

for line in lines:
    while r := re.search(r"\([^\(\)]+\)", line):
        line = line.replace(r.group(0), treat_par(r.group(0)))
        print(line)
    line = treat_par(line)
    grand_total += int(line)
    print(line)

print(grand_total)