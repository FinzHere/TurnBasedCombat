import random as rd
import os
import json
import time
import msvcrt
import sys
import enemies

def is_folder_empty(path):
    return not os.listdir(path)

weapons = {
    "Rusty Sword":5,
}

spells = {

}

armor = {

}

current_profile = 1

mainmenucon = True
gameloop = True
fighting = True
player_turn = True
enemy_turn = False

stop = False

has_encountered = False

player_dict = {
    "player_name":"Placeholder",
    "max_hp":25,
    "current_hp":25,
    "melee":1.00,
    "magicatk":1.00,
    "max_mana":15,
    "current_mana":15,
    "weapons":weapons,
    "armor":armor,
    "current_weapon":"Rusty Sword",
    "current_armor":"",
    "level":1,
    "exp":0,
    "enemies_killed":0,
    "spells":spells,
    "enemy_dificulty":1,
}

show_player_dict = {
    "player_name":"Placeholder",
    "max_hp":25,
    "current_hp":25,
    "melee":1.00,
    "magicatk":1.00,
    "max_mana":15,
    "current_mana":15,
    "weapons":weapons,
    "armor":armor,
    "current_weapon":"Rusty Sword",
    "current_armor":"",
    "level":1,
    "exp":0,
    "enemies_killed":0,
    "spells":spells,
}

descriptive_names = {
    "player_name":"NAME",
    "max_hp":"MAX HP",
    "current_hp":"CURRENT HP",
    "melee":"WEAPON ATTACK MULTIPLIER",
    "magicatk":"MAGIC ATTACK MULTIPLIER",
    "max_mana":"MAX MANA (your total amount of magic)",
    "current_mana":"CURRENT MANA (your magic left)",
    "weapons":"WEAPONS",
    "armor":"ARMOR",
    "current_weapon":"CURRENT WEAPON",
    "current_armor":"CURRENT ARMOR",
    "level":"LEVEL",
    "exp":"EXP",
    "enemies_killed":"ENEMIES KILLED",
    "spells":"SPELLS",
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
    def __init__(self, player_name: str, max_hp: float, current_hp: float, melee: float, magicatk: float, max_mana: float, current_mana: float, weapons: dict, armor: dict, current_weapon: str, current_armor: str, level: int, exp: int, enemies_killed: int, spells: dict, enemy_dificulty: float):
        self.player_name = player_name
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.melee = melee
        self.magicatk = magicatk
        self.max_mana = max_mana
        self.current_mana = current_mana
        self.weapons = weapons
        self.armor = armor
        self.current_weapon = current_weapon
        self.current_armor = current_armor
        self.level = level
        self.exp = exp
        self.enemies_killed = enemies_killed
        self.spells = spells
        self.enemy_dificulty = enemy_dificulty

    def save(self):
        file = f"Saves/P{str(current_profile)}.json"
        with open(file, "w") as f:
            json.dump(self.__dict__, f, indent=4)
        
        print("\nYou saved your game!")

    def load(self, pn: int):
        file = f"Saves/P{pn}.json"
        with open(file, "r") as f:
            player_dict = json.load(f)
            self.__dict__.update(player_dict)
            current_profile = pn
    
    def attack(self, enemy_health):
        print(enemy_health)
        key = self.current_weapon
        try:
            damage = self.weapons[key]
            damage = float(damage)
            damage = damage * self.melee
            enemy_health = enemy_health - damage
            enemy_health = round(enemy_health, 1)
            print(f"{enemy_health}")
            return enemy_health
        except KeyError:
            print("It did not work bc my coding is bad lol")

    def useSpell(self):
        print("Your Spells:")
        for key in self.spells:
            print(key)
        schoice = str(input("Pick a spell or put"))

    def level_up(self):
        while True:
            exp_needed = int((self.level + 5) * 1.2)

            if self.exp >= exp_needed:
                os.system('cls' if os.name == 'nt' else 'clear')

                self.exp -= exp_needed
                self.level += 1

                print(f"You Leveled Up! You are now level {self.level}\n")
                time.sleep(2)
            else:
                break
    
    def die(self):
        if round(self.current_hp, 1) <= 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("--- YOU DIED ---\n")
            print(f"\nPROFILE: {current_profile}")
            print(f"\nNAME: {self.player_name}")
            print(f"\nENEMIES KILLED: {self.enemies_killed}")
            print(f"\nLEVEL: {self.level}")
            print(f"\nMAX HP: {self.max_hp}")
            print(f"\nMAX MANA: {self.max_mana}")
            print(f"\nCURRENT WEAPON: {self.current_weapon}")
            print(f"\nCURRENT ARMOR: {self.current_armor}")
            print(f"\nALL WEAPONS:")
            for key in self.weapons:
                print(key)
            print(f"\nALL ARMOR: ")
            for key in self.armor:
                print(key)
            print(f"\nALL SPELLS: ")
            for key in self.spells:
                print(key)
            print(f"\nMELEE ATTACK MULTI: {round(self.melee, 2)}")
            print(f"\nMAGIC ATTACK MULTI: {round(self.magicatk, 2)}")
            print(f"\nENEMY DIFICULTY: {round(self.enemy_dificulty, 2)}")
            dpath = f"Saves/P{current_profile}.json"
            input("\n\n\nYour journey is unfortunately over. Press anything to end.")
            os.remove(dpath)
            print("Deletion complete!")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Goodbye, traveller!")
            sys.exit()
            return True
        else:
            return False

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
                    player = Player("", 0, 0, 0, 0, 0, 0, {}, {}, "", "", 0, 0, 0, {}, 0)
                    player.__dict__.update(player_dict)
                    mainmenucon = False
                    break
                elif os.path.exists("Saves/P1.json"):
                    player = Player("", 0, 0, 0, 0, 0, 0, {}, {}, "", "", 0, 0, 0, {}), 0
                    player.load(1)
                    print(f"\nSuccessfully loaded Profile {current_profile}!")
                    mainmenucon = False
                    break
            elif profile == "2":
                if not(os.path.exists("Saves/P2.json")):
                    create_profile(2)
                    player = Player("", 0, 0, 0, 0, 0, 0, {}, {}, "", "", 0, 0, 0, {}, 0)
                    player.__dict__.update(player_dict)
                    mainmenucon = False
                    break
                elif os.path.exists("Saves/P2.json"):
                    player = Player("", 0, 0, 0, 0, 0, 0, {}, {}, "", "", 0, 0, 0, {}, 0)
                    player.load(2)
                    print(f"\nSuccessfully loaded Profile {current_profile}!")
                    mainmenucon = False
                    break
            elif profile == "3":
                if not(os.path.exists("Saves/P3.json")):
                    create_profile(3)
                    player = Player("", 0, 0, 0, 0, 0, 0, {}, {}, "", "", 0, 0, 0, {}, 0)
                    player.__dict__.update(player_dict)
                    mainmenucon = False
                    break
                elif os.path.exists("Saves/P3.json"):
                    player = Player("", 0, 0, 0, 0, 0, 0, {}, {}, "", "", 0, 0, 0, {}, 0)
                    player.load(3)
                    print(f"\nSuccessfully loaded Profile {current_profile}!")
                    mainmenucon = False
                    break
    elif mainmenu == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        if os.path.exists("Saves/P1.json"):
            with open("Saves/P1.json", "r") as f:
                show_player_dict = json.load(f)
            print("--- PROFILE 1 STATISTICS ---")
            for key, value in show_player_dict.items():
                if not(key == "enemy_dificulty"):
                    label = descriptive_names.get(key, key)
                    print(f"{label}: {value}")
            print("\n")
        else:
            print("--- PROFILE 1 - EMPTY ---")
            print("\n")
        if os.path.exists("Saves/P2.json"):
            with open("Saves/P2.json", "r") as f:
                show_player_dict = json.load(f)
            print("--- PROFILE 2 STATISTICS ---")
            for key, value in show_player_dict.items():
                label = descriptive_names.get(key, key)
                print(f"{label}: {value}")
            print("\n")
        else:
            print("--- PROFILE 2 - EMPTY ---")
            print("\n")
        if os.path.exists("Saves/P3.json"):
            with open("Saves/P3.json", "r") as f:
                show_player_dict = json.load(f)
            print("--- PROFILE 3 STATISTICS ---")
            for key, value in show_player_dict.items():
                label = descriptive_names.get(key, key)
                print(f"{label}: {value}")
            print("\n")
        else:
            print("--- PROFILE 3 - EMPTY ---")
            print("\n")
    elif mainmenu == "3":
        print("Goodbye, traveller!")
        sys.exit()
    else:
        print("You did not give a valid input! Please pick one of the provided options!")

os.system('cls' if os.name == 'nt' else 'clear')
enemy = enemies.Enemy("", 1, 1, {}, 1, 1)
input_t = "1-Play game, 2-Change Weapon, 3-Save, 4-Save and Quit\n"

while True:
    player.level_up()
    if player.enemies_killed >= 1:
        input_t = "1-Continue game, 2-Change Weapon, 3-Save, 4-Save and Quit\n"
    play = str(input(input_t).strip())
    if play == "2":
        if len(player.weapons) >1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nALL WEAPONS\n")
            for k, v in player.weapons.items():
                print(f"{k} - DAMAGE: {v}")
            while True:
                new_weapon = str(input("Spell and Capitalize your new Weapon below to Equip it, or enter b to go back!!\n"))
                if new_weapon in player.weapons:
                    player.current_weapon = new_weapon
                    print(f"Successfully Equiped {player.current_weapon}")
                    break
                elif new_weapon in ["b", "back", "Back", "B"]:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                else:
                    print(f"Sorry, \"{new_weapon}\" was not a recognised input. Please make sure the spelling is correct!")
        else:
            print("You only have one weapon!")

    elif play == "3":
        player.save()
    elif play == "4":
        player.save()
        print("\nGoodbye, traveller!")
        sys.exit()
    elif play == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        while gameloop:
            enemy.spawn()
            fighting = True
            has_encountered = False
            enemy_turn = False
            player_turn = True
            stop = False
            while fighting:
                if has_encountered == False:
                    print(f"You encountered a wild {enemy.name}!")
                    has_encountered = True
                    time.sleep(1.75)
                while enemy_turn and (not(stop)):
                    eattack = enemy.attackPlayer()
                    if eattack["type"] == "heal":
                        enemy.current_health += eattack["amount"]
                        enemy.current_health = min(enemy.current_health, enemy.max_health)
                        enemy.current_health = round(enemy.current_health, 1)
                        print(enemy.current_health)
                        time.sleep(1.5)
                        player_turn = True
                        enemy_turn = False
                    elif eattack["type"] == "damage":
                        player.current_hp -= eattack["amount"]
                        if player.current_hp > 0:
                            print(f"Your health is now {player.current_hp}!")
                            time.sleep(1.5)
                    
                    player_turn = True
                    enemy_turn = False

                if player.die():
                    gameloop = False
                    fighting = False
                    enemy_turn = False
                    player_turn = False
                    stop = True

                print(f"{enemy.name} HEALTH: {enemy.current_health}")

                while player_turn and (not(stop)):
                    print("\nWhat would you like to do?")
                    if player.spells:
                        q = "1-Attack, 2-Block, 3-Use a Spell"
                    elif not(player.spells):
                        q = "1-Attack, 2-Block"

                    choice = str(input(q))
                    if choice == "1":
                        enemy.current_health = player.attack(enemy.current_health)
            
                    if choice == "2":
                        print(f"You blocked {enemy.name}'s attack!")
                        continue

                    enemy_turn = True
                    player_turn = False

                if enemy.die():
                    gameloop = False
                    fighting = False
                    player.enemies_killed += 1
                    stop = True
                    player.exp += enemy.exp
                    time.sleep(3)
                    os.system('cls' if os.name == 'nt' else 'clear')
