import re

with open("input", "r") as f:
    rules = f.read().splitlines()

def expand(sentence):
    sentence = list(sentence)
    infos = re.finditer(r"(\d+ [a-z]+ [a-z]+ bags?)", "".join(sentence))
    infos = sorted(infos, key=lambda x: x.span()[0], reverse=True)
    for info in infos:
        number, color = re.search(r"(\d+) ([a-z]+ [a-z]+) bags?", info.group(0)).groups()
        number = int(number)
        if number > 1:
            new_info = ", ".join([f"1 {color} bag"] * number)
        else:
            rule = next(r for r in rules if r.startswith(f"{color} bags contain"))
            if "no other bags" in rule:
                new_info = f"{info.group(0).replace(' bag', ' opened bag')}"
            else:
                new_info = f"{info.group(0).replace(' bag', ' opened bag')}, " + " ".join(rule.split(" ")[4:])[:-1]
        a, b = info.span()
        sentence[a:b] = new_info

    return "".join(sentence)

sentence = "shiny gold bags contain 4 pale black bags, 4 dim violet bags, 3 muted yellow bags."

while True:
    new_sentence = expand(sentence)
    if len(sentence) == len(new_sentence):
        print(sentence)
        break
    sentence = new_sentence