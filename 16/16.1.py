with open("input", "r") as f:
    lines = f.read().splitlines()

rules = {}
tickets = []

for line in lines:
    line = line.strip()
    if not line:
        continue
    if "ticket" in line:
        continue
    if not line[0].isdigit(): # rule
        name = line.split(":")[0]
        ab = line.split(" ")[-3]
        cd = line.split(" ")[-1]
        a, b = ab.split("-")
        c, d = cd.split("-")
        a, b, c, d = map(int, (a, b, c, d))
        rules[name] = (a,b,c,d)
    else: # ticket
        tickets.append(line)

invalid = []

for ticket in tickets[1:]: # ignoring my own ticket
    values = ticket.split(",")
    values = map(int, values)
    for value in values:
        valid = False
        for rule in rules:
            a, b, c, d = rules[rule]
            if a <= value <= b or c <= value <= d:
                valid = True
        if not valid:
            invalid.append(value)

print(sum(invalid))