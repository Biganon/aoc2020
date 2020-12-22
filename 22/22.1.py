from copy import deepcopy
import sys

with open("input", "r") as f:
    lines = f.read().splitlines()

p1 = []
p2 = []
receiving = p1
for idx, line in enumerate(lines):
    if not line:
        continue
    if "Player" in line:
        if "2" in line:
            receiving = p2
        continue
    n = int(line)

    if idx <= 25:
        receiving.append(n)
    else:
        receiving.append(n)

def game(p1, p2):
    round_idx = 0
    while True:
        round_idx += 1
        print(f"-- Round {round_idx} --", file=sys.stderr)
        print(f"Player 1's deck ({len(p1)}): {p1}", file=sys.stderr)
        print(f"Player 2's deck ({len(p2)}): {p2}", file=sys.stderr)
        
        c1 = p1.pop(0)
        c2 = p2.pop(0)

        print(f"Player 1 plays {c1}", file=sys.stderr)
        print(f"Player 2 plays {c2}", file=sys.stderr)

        if c1 > c2:
            round_winner = 1
        else:
            round_winner = 2
        print(f"Player {round_winner} wins round {round_idx}", file=sys.stderr)
        
        if round_winner == 1:
            p1.extend([c1, c2])
        else:
            p2.extend([c2, c1])

        if len(p1) == 0:
            game_winner = 2
            break
        if len(p2) == 0:
            game_winner = 1
            break
        
    print(f"Player {game_winner} wins the game", file=sys.stderr)
    return game_winner

winner = game(p1, p2)

winning_deck = {1:p1, 2:p2}[winner]

winning_deck = winning_deck[::-1]
total = 0
for idx, card in enumerate(winning_deck):
    total += (idx+1)*card
print(total)