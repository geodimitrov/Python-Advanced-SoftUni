BOMBS = {"Datura Bombs": 40, "Cherry Bombs": 60, "Smoke Decoy Bombs": 120}
TARGET = 9

def read_input():
    return [int(el) for el in input().split(", ")]

def valid_bomb_sum(bomb_sum, BOMBS, bombs_count):
    is_valid = False
    for key, value in BOMBS.items():
        if bomb_sum == value:
            bombs_count[key] += 1
            is_valid = True
    return is_valid

def reached_target(bombs_count):
    is_valid = True
    for value in bombs_count.values():
        if not value >= 3:
            is_valid = False
    return is_valid

def process_effects_and_casings(effects, casings):

    while effects and casings:
        bomb_effect = effects[0]
        bomb_casing = casings[-1]
        bomb_sum = bomb_effect + bomb_casing

        if valid_bomb_sum(bomb_sum, BOMBS, bombs_count):
            effects.pop(0)
            casings.pop()
        else:
            casings[-1] -= 5

        if reached_target(bombs_count):
            break

def print_result(bombs_count, effects, casings):
    if reached_target(bombs_count):
        print("Bene! You have successfully filled the bomb pouch!")
    else:
        print("You don't have enough materials to fill the bomb pouch.")

    if effects:
        print(f'Bomb Effects: {", ".join(map(str, effects))}')
    else:
        print("Bomb Effects: empty")

    if casings:
        print(f'Bomb Casings: {", ".join(map(str, casings))}')
    else:
        print("Bomb Casings: empty")

    for key, value in sorted(bombs_count.items()):
        print(f"{key}: {value}")

effects = read_input()
casings = read_input()
bombs_count = {key: 0 for key in BOMBS.keys()}
process_effects_and_casings(effects, casings)
print_result(bombs_count, effects, casings)