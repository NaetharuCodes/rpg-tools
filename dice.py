# RPG Dice Roller
# Rolls n dice of m sides
# If max_only set returns the highest result
# If min_only set returns the lowest result
# Otherwise returns a list of all results


import random

def dice(sides):

    return random.randrange(1, sides);

def roll_dice(num_dice : int, dice_size : int, max_only : bool = False, min_only : bool = False):

    results = [dice(dice_size) for _ in range(num_dice)]
    return max(results) if max_only else results


test = roll_dice(10, 4)

print(test)

test2 = roll_dice(6, 4, True)

print(test2)