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

next_game_idx = 0
def game(p1, p2):
    global next_game_idx
    next_game_idx += 1
    game_idx = next_game_idx
    print(f"=== Game {game_idx} ===", file=sys.stderr)
    states = set()
    # game_winner = None
    round_idx = 0
    while True: # rounds
        round_idx += 1
        print(f"-- Round {round_idx} of game {game_idx} --", file=sys.stderr)
        print(f"Player 1's deck ({len(p1)}): {p1}", file=sys.stderr)
        print(f"Player 2's deck ({len(p2)}): {p2}", file=sys.stderr)
        if (tuple(p1), tuple(p2)) in states:
            game_winner = 1
            print(f"Player 1 wins game {game_idx} (state already seen)", file=sys.stderr)
            break
        
        states.add((tuple(p1), tuple(p2)))
        print(f"{len(states)} states at this point", file=sys.stderr)

        c1 = p1.pop(0)
        c2 = p2.pop(0)

        print(f"Player 1 plays {c1}", file=sys.stderr)
        print(f"Player 2 plays {c2}", file=sys.stderr)

        if len(p1) >= c1 and len(p2) >= c2:
            print("New game needed to determine round winner...", file=sys.stderr)
            round_winner = game(p1[:c1], p2[:c2])
            print(f"Player {round_winner} wins round {round_idx} of game {game_idx} (sub-game)", file=sys.stderr)
        else:
            if c1 > c2:
                round_winner = 1
            else:
                round_winner = 2
            print(f"Player {round_winner} wins round {round_idx} of game {game_idx} (stronger card)", file=sys.stderr)
        
        if round_winner == 1:
            p1.extend([c1, c2])
        else:
            p2.extend([c2, c1])

        if len(p1) == 0:
            game_winner = 2
            print(f"Player 2 wins game {game_idx} (took all the cards)", file=sys.stderr)
            break
        if len(p2) == 0:
            game_winner = 1
            print(f"Player 1 wins game {game_idx} (took all the cards)", file=sys.stderr)
            break
    return game_winner

winner = game(p1, p2)

winning_deck = {1:p1, 2:p2}[winner]

winning_deck = winning_deck[::-1]
total = 0
for idx, card in enumerate(winning_deck):
    total += (idx+1)*card
print(total)