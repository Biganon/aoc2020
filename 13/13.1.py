#not_before = 939
#lines = (7,13,59,31,19)

not_before = 1000066
lines = (13,41,37,659,19,23,29,409,17)

waiting_times = {}

for line in lines:
    departure = 0
    while True:
        departure += line
        if departure >= not_before:
            waiting_times[line] = departure - not_before
            break

print(waiting_times)