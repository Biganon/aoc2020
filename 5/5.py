with open("input", "r") as f:
    lines = f.read().splitlines()

seat_ids = []

for line in lines:
    fb = line[:7]
    r1 = 0
    r2 = 127

    for i in fb:
        half = (r2-r1+1) / 2
        if i == "F":
            r2 -= half
        elif i == "B":
            r1 += half

    lr = line[7:]
    c1 = 0
    c2 = 7
    
    for j in lr:
        half = (c2-c1+1) / 2
        if j == "L":
            c2 -= half
        elif j == "R":
            c1 += half

    seat_ids.append(int(r1*8 + c1))

highest = max(seat_ids)

print(highest)

for x in range(min(seat_ids), highest):
    if x not in seat_ids:
        print(x)