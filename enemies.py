import json
import random as rd
import os

slime = {
    "name":"Slime",
    "max_health":9.8,
    "current_health":9.8,
    "attacks":{
        "Bounce":2.5,
        "Heal":0.7,
        "Do Nothing":0,
        "Bite":3,
    },
    "attack":1,
    "exp": 5,
}

goblin = {
    "name":"Goblin",
    "max_health":13.5,
    "current_health":13.5,
    "attacks":{
        "Charge":3.5,
        "Heal":1.3,
        "it's Pickaxe":5.5,
        "Bite":3,
    },
    "attack":1,
    "exp": 10,
}


enemiesg1 = [slime, goblin]
attack = 1
attack = float(attack)

class Enemy:
    def __init__(self, name: str, max_health: float, current_health: float, attacks: dict, attack: float, exp: int):
        self.name = name
        self.max_health = max_health
        self.current_health = current_health
        self.attacks = attacks
        self.attack = attack
        self.exp = exp

    def spawn(self, ek: int):
        if ek <= 3:
            newenemy = slime
        else:
            newenemy = rd.choice(enemiesg1)
        self.__dict__.update(newenemy)
        self.attack = attack
    
    def attackPlayer(self):
        sattack = rd.choice(list(self.attacks.keys()))

        if sattack == "Heal":
            heal_amount = float(self.attacks[sattack]) * self.attack
            heal_amount = round(heal_amount, 1)
            print(f"{self.name} healed for {heal_amount}!")
            return {"type": "heal", "amount": heal_amount}
        else:
            damage = float(self.attacks[sattack]) * self.attack
            damage = round(damage, 1)
            print(f"{self.name} used {sattack} and dealt {damage} damage!")
            return {"type": "damage", "amount": damage}

    def die(self):
        if self.current_health <= 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"You defeated {self.name}!")
            return True
        return False
