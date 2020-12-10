with open("input", "r") as f:
    adapters = f.read().splitlines()

adapters = sorted(map(int, adapters))

device = max(adapters) + 3

jolts = [0] + adapters + [device]

differences = []

for i in range(len(jolts)-1):
    a = jolts[i]
    b = jolts[i+1]
    differences.append(b-a)

print(differences.count(1) * differences.count(3))