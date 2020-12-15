numbers = [18,8,0,5,4,1,20]
#numbers = [0, 3, 6]
last_appearance = dict((x, numbers.index(x)+1) for x in numbers)

turn = len(numbers)
while True:
    turn += 1
    previous = numbers[-1]
    if previous not in last_appearance:
        last_appearance[previous] = turn-1
        numbers.append(0)
    else:
        delta = (turn-1) - last_appearance[previous]
        last_appearance[previous] = turn-1
        numbers.append(delta)
    if turn == 2020:
        print(numbers[-1])
        break