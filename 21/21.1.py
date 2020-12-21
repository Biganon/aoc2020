import re
from itertools import combinations
from collections import defaultdict

with open("input", "r") as f:
    lines = f.read().splitlines()

foods = []
ingredients = set()

for line in lines:
    i = re.search(r"(.*) \(", line).group(1)
    i = set(i.split(" "))
    ingredients.update(i)
    a = re.search(r"\(contains (.*)\)", line).group(1)
    a = set(a.split(", "))
    foods.append([i, a])

#######

bad_ingredients = set()

while True:
    contaminations = defaultdict(lambda: ingredients)

    pairs = combinations(foods, 2)
    for pair in pairs:
        a, b = pair
        a[0] -= {x[0] for x in bad_ingredients}
        b[0] -= {x[0] for x in bad_ingredients}
        a[1] -= {x[1] for x in bad_ingredients}
        b[1] -= {x[1] for x in bad_ingredients}
        iic = a[0].intersection(b[0])
        aic = a[1].intersection(b[1])
        for allergen in aic:
            contaminations[allergen] = contaminations[allergen].intersection(iic)

    for (k,v) in [(k,v) for (k,v) in contaminations.items() if len(v) == 1]:
        bad_ingredients.add(  (  list(v)[0], k  ) )

    if len(contaminations) == 0:
        break

total = 0
for food in foods:
    ingredients = food[0]
    total += len(ingredients)
print(total)