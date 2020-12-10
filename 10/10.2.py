from collections import defaultdict

with open("input", "r") as f:
    adapters = f.read().splitlines()

adapters = sorted(map(int, adapters))

device = max(adapters) + 3

jolts = [0] + adapters + [device]

ways = defaultdict(lambda:0)
ways[0] = 1

for i in range(1, len(jolts)):
    ways[jolts[i]] = ways[jolts[i]-1] + ways[jolts[i]-2] + ways[jolts[i]-3]

print(ways[jolts[-1]])