import re
from math import prod

with open("input", "r") as f:
    lines = f.read().splitlines()

def treat_par(par):
    if par[0] == "(":
        par = par[1:]
    if par[-1] == ")":
        par = par[:-1]

    additions = re.finditer(r"\d+(?: \+ \d+)+", par)
    for addition in sorted(additions, key=lambda x:x.start(), reverse=True):
        a = addition.start()
        b = addition.end()
        s = sum(map(int, addition.group(0).split("+")))
        par = par[:a] + str(s) + par[b:]
    total = prod(map(int, par.split("*")))
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