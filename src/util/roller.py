
import random


def roll(roll: str) -> dict:

    dice = []
    total = 0
    drop_modifier = 0
    addition_mod = 0
    subtraction_mod = 0

    if '(' in roll:
        deconstructed_roll = roll.split('(')
        roll = deconstructed_roll[0]
        modifier = deconstructed_roll[1]
        modifier = modifier.replace(')','')
        drop_modifier = int(modifier)
    
    if '+' in roll:
        temp = roll.split('+')
        roll = temp[0]
        addition_mod = int(temp[1])

    if '-' in roll:
        temp = roll.split('-')
        roll = temp[0]
        subtraction_mod = int(temp[1])

    parts = roll.split('d')

    dice_to_roll = int(parts[0])
    type_to_roll = int(parts[1])

    for i in range(0,dice_to_roll):
        dice.append(random.randrange(1,type_to_roll))

    if drop_modifier > 0:
        s_dice = sorted(dice, reverse=True)
        for i in range(0,drop_modifier):
            total += s_dice[i] 
    else:
        for r in dice:
            total += r

    total += addition_mod
    total -= subtraction_mod

    return {
        "dice": dice,
        "result": total
    }