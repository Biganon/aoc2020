import re

with open("input", "r") as f:
    rules = f.read().splitlines()

can_contain_gold = set()

def get_containers(color):
    for rule in rules:
        if r := re.search(rf"^(.*) bags contain.*{color}", rule):
            can_contain_gold.add(r.group(1))
            get_containers(r.group(1))

get_containers("shiny gold")

print(len(can_contain_gold))