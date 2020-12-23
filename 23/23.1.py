import sys
from time import time

my_input = "215694783"
example = "389125467"

def play(cups, iterations):
    max_ = max(cups)
    circle = {}
    for i in range(len(cups)-1):
        circle[cups[i]] = cups[i+1]
    circle[cups[-1]] = cups[0]
    current = circle[cups[-1]]

    for _ in range(iterations):
        picked_up = []
        next_ = current
        for _ in range(3):
            next_ = circle[next_]
            picked_up.append(next_)

        destination = current
        while True:
            destination -= 1
            if destination < 1:
                destination = int(max_)
            if destination not in picked_up:
                break

        temp = circle[picked_up[-1]]
        circle[picked_up[-1]] = circle[destination]
        circle[destination] = picked_up[0]
        circle[current] = temp

        current = circle[current]

    a = 1
    for _ in range(len(cups)-1):
        print(circle[a], end="")
        a = circle[a]
    print()

play(list(map(int, list(my_input))), 100)