import monsterType
import characterCreation

bttleDeci = '\n1. Attack\n'

def battle(player):
    print(f"You have entered battle \nYou are battling a {monsterType.Goblin.name}")
    while monsterType.Goblin.health > 0:
        deci = input(f"What will you do {bttleDeci}")
        if deci == '1':
            print(f"You did {characterCreation.character1.type.attr['attack']} damage")






battle(characterCreation.character())