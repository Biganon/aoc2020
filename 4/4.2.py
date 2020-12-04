import re

with open("input2", "r") as f:
    lines = f.read().splitlines()

total = 0

for line in lines:
    data = dict(x.split(":") for x in line.split(","))
    if not 1920 <= int(data["byr"]) <= 2002:
        continue
    if not 2010 <= int(data["iyr"]) <= 2020:
        continue
    if not 2020 <= int(data["eyr"]) <= 2030:
        continue
    if not re.match(r"\d+(cm|in)", data["hgt"]):
        continue
    if not {"cm":150,"in":59}[data["hgt"][-2:]] <= int(data["hgt"][:-2]) <= {"cm":193,"in":76}[data["hgt"][-2:]]:
        continue
    if not re.match(r"#[0-9a-f]{6}", data["hcl"]):
        continue
    if not data["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
        continue
    if not re.fullmatch(r"\d{9}", data["pid"]):
        continue
    total += 1

print(total)