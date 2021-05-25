'''
character creation where the user will decide what they want to play as

class - tank, wizard, warrior, priest
'''

import time

def character():
    n = create_name()
    t = create_type()
    charcter1 = player(n, t)
    print(f'Your name is {n} and you are a {t}')
    return charcter1





def create_name():
    print("Hello!")
    time.sleep(1)
    nd = 1
    name = ''
    while nd > 0:
        name = input("Welcome to Heaven's Gates! What would you like your name to be:\n")
        name_decide = input(f'Your name is {name}. Is this correct? (y/n):\n')
        if name_decide == 'y':
            print("Great! Now you will move onto your class decision")
            nd -= 1
        elif name_decide == 'n':
            pass
        else:
            print("That was an invalid input. Please input your name, than 'y' or 'n' to confirm your name.")
    return name





def create_type():
    print(f'Welcome, we will now decide your class.')
    td = False
    while td == False:
        type = input("What would you like to be:\n1. Tank\n2. Wizard\n3. Warrior\n4. Priest\nPlease select 1-4:")
        if type == '1':
            print("You are now a tank")
            return "Tank"
        elif type == '2':
            print("Your are now a wizard")
            return "Wizard"
        elif type == '3':
            print("You are now a warrior")
            return "Warrior"
        elif type == '4':
            print("You are now a priest")
            return "Priest"








class player:
    def __init__(self, name, type):
        self.name = name
        self.type = type



class tank(player):
    attr = {'health': 45, 'attack': 20, 'moves': ['Kick', 'Shield Bash', 'Smite']}

class wizard(player):
    attr = {'health': 30, 'attack': 35, 'moves': ['Lightning', 'Flame', 'Magic Blast']}

class warrior(player):
    attr = {'health': 40, 'attack': 25, 'moves': ['Sword Slash', 'Impale', 'Ground Slam']}

class priest(player):
    attr = {'health': 40, 'attack': 25, 'moves': ['Heal', 'Ball of Light', 'Heavenly Smash']}




player1 = player(create_name(), create_type())
