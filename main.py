class Player():
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp 
        self.dmg = dmg

    def attack(self, target):
        target.take_dmg(self.dmg)

    def take_dmg(self, dmg):
        self.hp -= dmg

class Monster():
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp 
        self.dmg = dmg
    
    def attack(self, target):
        target.take_dmg(self.dmg)

    def take_dmg(self, dmg):
        self.hp -= dmg


player = Player('Artem', 100, 13)
monster = Monster('Natali', 110, 24) 

print(player.hp)

monster.attack(player)

print(player.hp)
print(monster.dmg)