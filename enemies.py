import json
import random as rd
import os

slime = {
    "name":"Slime",
    "max_health":9.8,
    "current_health":9.8,
    "attacks":{
        "Bounce":2.5,
        "hHeal":0.7,
        "Do Nothing":0,
        "Bite":3,
    },
    "attack":1,
    "exp": 5,
}
RockGolem = {
    "name":"Rock Golem",
    "max_health":15.676767,
    "current_health":15,
    "attacks":{
        "Slam":8,
        "hRock Regenerate":0.7,
        "Do Nothing": 0,
        "Chew":5,
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
        "hHeal":1.3,
        "it's Pickaxe":6.25,
        "Bite":3,
    },
    "attack":1,
    "exp": 10,
}


enemiesg1 = [slime, goblin]
enemiesg2 = [slime, goblin, RockGolem]
attack = 1
attack = round(attack, 2)


class Enemy:
    def __init__(self, name: str, max_health: float, current_health: float, attacks: dict, attack: float, exp: int):
        self.name = name
        self.max_health = max_health
        self.current_health = current_health
        self.attacks = attacks
        self.attack = attack
        self.exp = exp

    def spawn(self, ek: int, ed: float):
        if ek <= 3:
            newenemy = slime
        elif 3 < ek < 15:
            newenemy = rd.choice(enemiesg1)
        elif ek >= 15:
            newenemy = rd.choice(enemiesg2)
        else:
            newenemy = rd.choice(enemiesg1)
        newenemy["max_health"] = newenemy["max_health"] * ed
        newenemy["current_health"] = newenemy["current_health"] * ed
        newenemy["attack"] = newenemy["attack"] * ed
        newenemy["max_health"] = round(newenemy["max_health"], 2)
        newenemy["current_health"] = round(newenemy["current_health"], 2)
        newenemy["attack"] = round(newenemy["attack"], 2)
        self.__dict__.update(newenemy)
    
    def attackPlayer(self):
        sattack = rd.choice(list(self.attacks.keys()))

        if sattack.startswith("h"):
            heal_amount = float(self.attacks[sattack]) * self.attack
            heal_amount = round(heal_amount, 1)
            print(f"{self.name} used {sattack[1:]} {heal_amount}!")
            return {"type": "heal", "amount": heal_amount}
        else:
            damage = float(self.attacks[sattack]) * self.attack
            damage = round(damage, 1)
            print(f"{self.name} used {sattack} and dealt {damage} damage!\n")
            return {"type": "damage", "amount": damage}

    def die(self):
        if self.current_health <= 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"You defeated {self.name}!")
            return True
        return False
