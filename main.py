import json, random

with open("player.json") as data:
    data_player = json.load(data)

class Player():
    def __init__(self, data):
        self.name = data["name"]
        self.hp = data["hp"]
        self.min_dmg = data["min_dmg"]
        self.max_dmg = data["max_dmg"]
        self.exp = data["exp"]

    def attack(self, target):
        target.take_dmg(random.randint(self.min_dmg, self.max_dmg))

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
        if self.hp < 0:
            self.hp = 0

player = Player(data_player)
monster = Monster('Natali', 110, 24) 

while monster.hp > 0:
    print(monster.hp)
    player.attack(monster)
else:
    print("You won")