from math import prod

with open("input", "r") as f:
    lines = f.read().splitlines()

rules = {}
fields = {}
tickets = []
valid_tickets = []

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

invalid_values = []

for ticket in tickets[1:]: # ignoring my own ticket
    values = ticket.split(",")
    values = map(int, values)
    ticket_is_valid = True
    for value in values:
        value_is_valid = False
        for rule in rules:
            a, b, c, d = rules[rule]
            if a <= value <= b or c <= value <= d:
                value_is_valid = True
        if not value_is_valid:
            invalid_values.append(value)
            ticket_is_valid = False
    if ticket_is_valid:
        valid_tickets.append(ticket)

nb_of_fields = len(valid_tickets[0].split(","))

for field in range(1, nb_of_fields):
    values = [ticket.split(",")[field] for ticket in valid_tickets]
    values = list(map(int, values))
    field_can_be = []
    for rule in rules:
        a, b, c, d = rules[rule]
        rule_works_for = 0
        for value in values:
            if a <= value <= b or c <= value <= d:
                rule_works_for += 1

        if rule_works_for == len(valid_tickets):
            field_can_be.append(rule)
    fields[field] = field_can_be

final = {}

while True:
    try:
        found_field = next(field for field in fields if len(fields[field]) == 1)
        found_rule = fields[found_field][0]
    except StopIteration:
        try:
            found_rule = next(rule for rule in rules if len([x for x in fields.values() if rule in x]) == 1)
            found_field = next(x for x in fields if found_rule in fields[x])
        except StopIteration:
            departures = [x[0] for x in final.items() if x[1].startswith("departure")]
            my_ticket = list(map(int, tickets[0].split(",")))
            print(prod(my_ticket[x] for x in departures))
            break

    final[found_field] = found_rule
    fields = {k:[x for x in v if x != found_rule] for (k,v) in fields.items() if k != found_field}