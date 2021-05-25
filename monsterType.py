class Monster:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

class Goblin(Monster):
    name = 'Goblin'
    health = 20
    damage = 10