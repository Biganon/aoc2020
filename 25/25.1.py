pk_card = 10441485
pk_door = 1004920

pk_card_example = 5764801
pk_door_example = 17807724

def find_loop_size(goal):
    value = 1
    loop_size = 0
    while True:
        loop_size += 1
        value *= 7
        value = value % 20201227
        if value == goal:
            return loop_size

loop_size_card = find_loop_size(pk_card)
loop_size_door = find_loop_size(pk_door)

def find_encryption_key(loop_size, public_key):
    value = 1
    for _ in range(loop_size):
        value *= public_key
        value = value % 20201227
    return value

encryption_key1 = find_encryption_key(loop_size_card, pk_door)
encryption_key2 = find_encryption_key(loop_size_door, pk_card)

assert encryption_key1 == encryption_key2

print(encryption_key1)