import re

with open("input2", "r") as f:
    lines = f.read().splitlines()

rules = [line for line in lines if line and line[0].isdigit()]
rules = dict((int(rule.split(": ")[0]), "("+rule.split(": ")[1]+")") for rule in rules)

strings = [line for line in lines if line and not line[0].isdigit()]

valid = set()
last_length = 0

rule0 = rules[0]
while any(x for x in rule0 if x.isdigit()):
    numbers = list(re.finditer(r"\d+", rule0))
    for number in sorted(numbers, key=lambda x:x.start(), reverse=True):
        a = number.start()
        b = number.end()
        rule0 = rule0[:a] + rules[int(number.group(0))] + rule0[b:]

    regex = rule0.replace(" ", "").replace('"', "")

    for string in strings:
        if re.search(rf"^{regex}$", string):
            valid.add(string)

    if len(valid) == last_length != 0:
        print(len(valid))
        break

    last_length = len(valid)