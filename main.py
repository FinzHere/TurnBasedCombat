import random as rd
import os
import json
import time
import msvcrt
import sys

def is_folder_empty(path):
    return not os.listdir(path)

weapons = {
    "Rusty Sword":"m5",
}

armor = {

}

current_profile = 1

mainmenucon = True

player_dict = {
    "player_name":"Placeholder",
    "max_hp":25,
    "current_hp":25,
    "melee":5,
    "magicatk":10,
    "mana":15,
    "weapons":weapons,
    "armor":armor,
    "current_weapon":"Rusty Sword",
    "current_armor":"",
    "level":1,
    "exp":0,
    "enemies_killed":0
}

def create_profile(pn: int):
    file = f"Saves/P{pn}.json"
    os.system('cls' if os.name == 'nt' else 'clear')
    newname = str(input("Tell me, what is your name?").strip().capitalize())
    player_dict["player_name"] = newname
    with open(file, "w") as f:
        json.dump(player_dict, f, indent=4)
    current_profile = pn

class Player:
    def __init__(self, player_name: str, max_hp: int, current_hp: int, melee: int, magicatk: int, mana: int, weapons: dict, armor: dict, current_weapon: str, current_armor: str, level: int, exp: int, enemies_killed: int,):
        self.player_name = player_name
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.melee = melee
        self.magicatk = magicatk
        self.mana = mana
        self.weapons = weapons
        self.armor = armor
        self.current_weapon = current_weapon
        self.current_armor = current_armor
        self.level = level
        self.exp = exp
        self.enemies_killed = enemies_killed

    def save(self):
        file = f"Saves/P{str(current_profile)}"
        with open(file, "w") as f:
            json.dump(self.__dict__, f, indent=4)
    def load(self, pn: int):
        file = f"Saves/P{pn}.json"
        with open(file, "r") as f:
            player_dict = json.load(f)
            self.__dict__.update(player_dict)
            current_profile = pn

os.makedirs("Saves", exist_ok=True)

os.system('cls' if os.name == 'nt' else 'clear')

print("A quick word of warning...")
time.sleep(2)
print("DO NOT JUST QUIT THE PROGRAM, YOUR GAME FILE WILL NOT SAVE. YOU CAN ONLY SAVE BETWEEN BATTLES!")
time.sleep(3.5)
os.system('cls' if os.name == 'nt' else 'clear')

print("RPG GAME")

while mainmenucon:
    print("\nWhat would you like to do?")
    mainmenu = str(input("1-Select Profile, 2-List Profile Stats, 3-Quit Game"))
    if mainmenu == "1":
        while True:
            profile = str(input("\nPlease pick profile 1, 2, or 3, or type \"back\" to go back!").strip().lower())
            if profile in ["b", "back"]:
                break
            elif profile == "1":
                if not(os.path.exists("Saves/P1.json")):
                    create_profile(1)
                    player = Player("", 0, 0, 0, 0, 0, {}, {}, "", "", 0, 0, 0)
                    player.__dict__.update(player_dict)
                    mainmenucon = False
                    break
                elif os.path.exists("Saves/P1.json"):
                    player = Player("", 0, 0, 0, 0, 0, {}, {}, "", "", 0, 0, 0)
                    player.load(1)
                    print(f"\nSuccessfully loaded Profile {current_profile}!")
                    print(player.player_name)
            elif profile == "2":
                if not(os.path.exists("Saves/P2.json")):
                    create_profile(2)
                    player = Player("", 0, 0, 0, 0, 0, {}, {}, "", "", 0, 0, 0)
                    player.__dict__.update(player_dict)
                    mainmenucon = False
                    break
                elif os.path.exists("Saves/P2.json"):
                    player = Player("", 0, 0, 0, 0, 0, {}, {}, "", "", 0, 0, 0)
                    player.load(2)
                    print(f"\nSuccessfully loaded Profile {current_profile}!")
                    print(player.player_name)
            elif profile == "3":
                if not(os.path.exists("Saves/P3.json")):
                    create_profile(3)
                    player = Player("", 0, 0, 0, 0, 0, {}, {}, "", "", 0, 0, 0)
                    player.__dict__.update(player_dict)
                    mainmenucon = False
                    break
                elif os.path.exists("Saves/P3.json"):
                    player = Player("", 0, 0, 0, 0, 0, {}, {}, "", "", 0, 0, 0)
                    player.load(3)
                    print(f"\nSuccessfully loaded Profile {current_profile}!")
    elif mainmenu == "2":
        print("Empty for now!")
    elif mainmenu == "3":
        print("Goodbye, traveller")
        sys.exit()
    else:
        print("You did not give a valid input! Please pick one of the provided options!")
                

