with open("input", "r") as f:
    data = f.read()

groups = data.split("\n\n")

total1 = 0
total2 = 0

for group in groups:
    answers = group.split("\n")
    one_line = "".join(answers)
    distinct_answers = set(one_line)
    universal_answers = [a for a in distinct_answers if one_line.count(a) == len(answers)]
    total1 += len(distinct_answers)
    total2 += len(universal_answers)

print(total1, total2)