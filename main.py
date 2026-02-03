import random as rd
import os
import json
import time
import sys
import enemies

weapons = {
    "Rusty Sword":5,
}

L10spells = {
    "Mana Burst": 5.5,
    "Astral Flare": 6.5,
    "Hex": 7.7,
    "Blightcast": 11,
}

spells = {

}

heal_spells = {}
with open("Items/HEALSPELLS.json") as f:
    heal_spells = json.load(f)

attack_spells = {}
with open("Items/ATTACKSPELLS.json") as f:
    attack_spells = json.load(f)

armor = {

}

items = {

}

spells_trigger = True
spell_unlock = False

current_profile = 1

item_counter = 0

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
    "items":items,
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
    "items":items,
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
    "items":"ITEMS",
}

def spellInform():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Spells are Powerful Magic Attacks, capable of MASSIVE damage!")
    time.sleep(2.5)
    print("Using a spell will use up your turn - be wise!")
    time.sleep(1.6)
    print("However, these abilities come with a cost - mana.")
    time.sleep(1.75)
    print("Mana is the amount of magic you have, and however much damage you deal is how much mana is used.")
    time.sleep(3)
    print("When you run out of mana, you can't use any spells.")
    time.sleep(2)
    print("Don't worry though, as you can gain back mana through level-ups and mana potions!")
    time.sleep(1)
    input("I hope this helped! Press enter to close this pop-up!")
    os.system('cls' if os.name == 'nt' else 'clear')

def create_profile(pn: int):
    file = f"Saves/P{pn}.json"
    os.system('cls' if os.name == 'nt' else 'clear')
    newname = str(input("Tell me, what is your name?").strip().capitalize())
    player_dict["player_name"] = newname
    with open(file, "w") as f:
        json.dump(player_dict, f, indent=4)
    current_profile = pn

class Player:
    def __init__(self, player_name: str, max_hp: float, current_hp: float, melee: float, magicatk: float, max_mana: float, current_mana: float, weapons: dict, armor: dict, current_weapon: str, current_armor: str, level: int, exp: int, enemies_killed: int, spells: dict, enemy_dificulty: float, items: dict,):
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
        self.items = items

    def rundown(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Hello, {self.player_name}!")
        print("This guide is here to tell you how to play the game! Press enter to get started! (once you have started the tutorial, press enter to skip it)")
        input()
        print(f"\nHOW TO PLAY:")
        print(f"\nBefore going into battle, which will be explained later, you will get some options. These include:")
        print(f"Playing\nChanging Weapon\nChanging Armor(not working yet)\nSaving\nQuiting")
        print(f"For changing weapons and armor, you will be taken to section where all of your weapons and armor are displayed, \nyou just have to input its name and you'll equip it.")
        print(f"For battling, that's what I'm about to get into.\n")
        print(f"\nBATTLING: ")
        print(f"\nIn a battle, you and an oppenent face of, exchanging attacks until only one of you is left standing. \nThere are 4 options you can take in a battle:")
        print(f"1-Attack with a weapon\n2-Block an incoming attack\n3-Use an item\n4-Run")
        print(f"\nWhen you attack, you attack with your currently equiped weapon.")
        print(f"When you block, you block the enemy's attack.")
        print(f"When you use an item, you can use one of your items. These include things like potions. When used, items take up your turn.")
        print(f"Running does what you think - you run from the battle.")
        print(f"\nOnce you have performed one of these actions, it's the enemy's turn.\n")
        print(f"\nENEMIES: ")
        print(f"\nEnemies in this game progress with you - as you grow stronger, so do they.")
        print(f"As you get further you will also start to encounter new enemies, which I'll leave it to you to find out what they are!\n")
        print(f"\nCHESTS: ")
        print(f"\nChests appear every few rounds, and they give you new items!")
        print(f"If you already have an item, don't worry! It will get a boost in it's base damage/amount.")
        print(f"Chests are very useful items, and they're there to help you. Utilize them to their full potential!\n")
        print(f"\n\n")
        print("UNRELEASED CONTENT: ")
        print(f"\nBOSSES: ")
        print(f"\nBosses are a planned feature that will appear every ten rounds, and they will be tougher than normal enemies.")
        print(f"Because of this, they will drop more loot and give more exp! They might even drop special items...")
        input("\n\nOnce you are ready, press enter!")
        os.system('cls' if os.name == 'nt' else 'clear')

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
            if self.current_hp > self.max_hp:
                print("PLAYER ACOUNT MODIFICATION DETECTED")
                time.sleep(2)
                print("Punishing Player for Cheating...")
                time.sleep(2)
                self.current_hp = self.max_hp
                self.current_hp = self.current_hp * 0.5
                print(f"{self.current_hp} is now your current hp!")
                time.sleep(2.5)
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
        print("\nYour Spells:\n")
        for key in self.spells:
            print(key)
        schoice = str(input("\nPick a spell or put back to go back! Spells have to be spelt and capitalized correctly to work!\n"))
        if schoice in ["b", "back", "B", "Back"]:
            return "back"
        elif schoice in self.spells:
            if self.spells[schoice]["type"] == "heal":
                amount = self.spells[schoice]["amount"]
                amount = float(amount) * self.magicatk
                amount = round(amount, 2)
                return {"type": "heal", "amount": float(amount), "name": schoice}
            elif self.spells[schoice]["type"] == "attack":
                amount = self.spells[schoice]["amount"]
                amount = float(amount) * self.magicatk
                amount = round(amount, 2)
                return {"type": "attack", "amount": float(amount), "name": schoice}
        else:
            print(f"\nSorry, {schoice} is not a recognised input. Please make sure that your spelling is correct and try again!")
            return "back"
    
    def useItem(self, enemy_health):
        print("YOUR ITEMS:")
        for key in self.items:
            print(key)
        print("Type the name of an item to use it, or put b to go back!")
        itemchoice = input()
        if itemchoice in ["b", "back", "B", "Back"]:
            return "back"
        elif (itemchoice in self.items) and item_counter == 0:
            item_counter = 3
            item_type = self.items[itemchoice]["type"]
            if item_type == "heal":
                amount = self.items[itemchoice]["amount"]
                return {"type": item_type, "amount": amount, "name": itemchoice}
            elif item_type == "strength":
                amount = self.items[itemchoice]["amount"]
                return {"type": item_type, "amount": amount, "name": itemchoice}
        elif (itemchoice in self.items):
            return "not_usable"
        else:
            return "not_recognised"

    def level_up(self):
        while True:
            exp_needed = int((self.level + 5) * 1.2)

            if self.level >= 10 and not(self.spells):
                print("You find a strange book...")
                time.sleep(2.75)
                print("It's a book of spells!")
                spellanswer = input("Would you like to learn how spells work? (y or yes to know)")
                if spellanswer in ["y", "yes"]:
                    spellInform()
                self.spells = L10spells
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You unlocked Spells!")
                time.sleep(1.5)
            elif self.exp >= exp_needed:
                os.system('cls' if os.name == 'nt' else 'clear')

                self.exp -= exp_needed
                self.level += 1

                print(f"You Leveled Up! You are now level {self.level}\n")
                self.enemy_dificulty += 0.1
                time.sleep(2)
            else:
                break

    def openChest(self):
        decider = rd.random()
        decider = round(decider, 2)
        if self.spells:
            if decider <= 0.4:
                itype = "WEAPONS"
            elif 0.41 <= decider <= 0.8:
                itype = "ITEMS"
            else:
                itype = "SPELLS"
        else:
            if decider <= 0.5:
                itype = "WEAPONS"
            else:
                itype = "ITEMS"
        rdecider = rd.random()
        rdecider = round(decider, 2)
        if rdecider <= 0.57:
            rarity = "COMMON"
        elif 0.58 <= rdecider <= 0.80:
            rarity = "UNCOMMON"
        elif 0.81 <= rdecider <= 0.95:
            rarity = "EPIC"
        else:
            rarity = "LEGENDARY"
        path = f"Items/{rarity}{itype}.json"
        print(f"You found a chest!")
        time.sleep(2)
        print(f"The rarity is {rarity}...")
        time.sleep(2.5)
        print(f"You got a...")
        with open(path, "r") as f:
            available_items: dict = json.load(f)
        weapon_name = rd.choice(list(available_items.keys()))
        to_add = available_items[weapon_name]
        if weapon_name in self.spells:
            print(f"You got {weapon_name}! It's a spell!")
            time.sleep(2)
            print(f"You already have {weapon_name}!")
            amount = self.spells[weapon_name]["amount"]
            amount = float(amount) + 0.2
            self.spells[weapon_name]["amount"] = amount
            time.sleep(1.5)
            print(f"You increased {weapon_name}'s power!")
        elif weapon_name in self.weapons:
            print(f"You got a {weapon_name}! It's a weapon!")
            time.sleep(2)
            print(f"You already have a {weapon_name}!")
            amount = self.weapons[weapon_name]
            amount = float(amount) + 0.2
            self.weapons[weapon_name] = amount
            time.sleep(1.5)
            print(f"You increased {weapon_name}'s power!")
        elif weapon_name in self.items:
            print(f"You got a {weapon_name}! It's an item!")
            time.sleep(2)
            print(f"You already have a {weapon_name}!")
            amount = self.items[weapon_name]["amount"]
            amount = float(amount) + 0.2
            self.items[weapon_name]["amount"] = amount
            time.sleep(1.5)
            print(f"You increased {weapon_name}'s power!")
        elif (itype.lower()) == "weapons":
            self.weapons[weapon_name] = to_add
            print(f"You got a {weapon_name} (weapon)!")
        elif (itype.lower()) == "spells":
            self.spells[weapon_name] = to_add
            print(f"You got a {weapon_name} (spell)!")
        elif (itype.lower()) == "items":
            self.items[weapon_name] = to_add
            print(f"You got a {weapon_name} (item)!")
    
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
            print(f"\nALL ITEMS: ")
            for key in self.items:
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
                    player = Player("", 0, 0, 0, 0, 0, 0, {}, {}, "", "", 0, 0, 0, {}, 0, {})
                    player.__dict__.update(player_dict)
                    mainmenucon = False
                    break
                elif os.path.exists("Saves/P1.json"):
                    player = Player("", 0, 0, 0, 0, 0, 0, {}, {}, "", "", 0, 0, 0, {}, 0, {})
                    player.load(1)
                    print(f"\nSuccessfully loaded Profile {current_profile}!")
                    mainmenucon = False
                    break
            elif profile == "2":
                if not(os.path.exists("Saves/P2.json")):
                    create_profile(2)
                    player = Player("", 0, 0, 0, 0, 0, 0, {}, {}, "", "", 0, 0, 0, {}, 0, {})
                    player.__dict__.update(player_dict)
                    mainmenucon = False
                    break
                elif os.path.exists("Saves/P2.json"):
                    player = Player("", 0, 0, 0, 0, 0, 0, {}, {}, "", "", 0, 0, 0, {}, 0, {})
                    player.load(2)
                    print(f"\nSuccessfully loaded Profile {current_profile}!")
                    mainmenucon = False
                    break
            elif profile == "3":
                if not(os.path.exists("Saves/P3.json")):
                    create_profile(3)
                    player = Player("", 0, 0, 0, 0, 0, 0, {}, {}, "", "", 0, 0, 0, {}, 0, {})
                    player.__dict__.update(player_dict)
                    mainmenucon = False
                    break
                elif os.path.exists("Saves/P3.json"):
                    player = Player("", 0, 0, 0, 0, 0, 0, {}, {}, "", "", 0, 0, 0, {}, 0, {})
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

if player.spells:
    spell_unlock = True

os.system('cls' if os.name == 'nt' else 'clear')
enemy = enemies.Enemy("", 1, 1, {}, 1, 1)
input_t = "1-Play game, 2-Change Weapon, 3-Save, 4-Save and Quit\n"

while True:
    player.level_up()
    if player.enemies_killed == 0:
        rundown = input("Would you like a rundown on how the game works (press y or yes to accept)?").strip().lower()
        if rundown in ["y", "yes"]:
            player.rundown()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
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
                new_weapon = str(input("Spell and Capitalize your new Weapon correctly below to Equip it, or enter b to go back!!\n"))
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
            print("You only have one weapon!\n")

    elif play == "3":
        player.save()
    elif play == "4":
        player.save()
        print("\nGoodbye, traveller!")
        sys.exit()
    elif play == "1":
        gameloop = True
        os.system('cls' if os.name == 'nt' else 'clear')
        while gameloop:
            enemy.spawn(player.enemies_killed, player.enemy_dificulty)
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
                        print(f"{enemy.name} HP is now {enemy.current_health}!\n")
                        time.sleep(1.5)
                        player_turn = True
                        enemy_turn = False
                    elif eattack["type"] == "damage":
                        player.current_hp -= eattack["amount"]
                        if player.current_hp > 0:
                            print(f"Your HP is now {player.current_hp}!\n")
                            time.sleep(1.5)
                    
                    player_turn = True
                    enemy_turn = False

                if player.die():
                    gameloop = False
                    fighting = False
                    enemy_turn = False
                    player_turn = False
                    stop = True

                print(f"\n{enemy.name} HEALTH: {enemy.current_health}")

                while player_turn and (not(stop)):
                    print("\nWhat would you like to do?")
                    if player.spells:
                        q = "1-Attack, 2-Block, 3-Use an Item, 4-Run, 5-Use a Spell"
                    elif not(player.spells):
                        q = "1-Attack, 2-Block, 3-Use an Item, 4-Run"

                    choice = str(input(q))
                    if choice == "1":
                        enemy.current_health = player.attack(enemy.current_health)
            
                    elif choice == "2":
                        print(f"You blocked {enemy.name}'s attack!")
                        continue

                    elif choice == "5" and player.spells:
                        spell = player.useSpell()
                        if spell == "back":
                            continue
                        elif spell["type"] == "heal":
                            amount_to_add = player.current_hp + spell["amount"]
                            amount_to_add = round(amount_to_add, 2)
                            player.current_hp = amount_to_add
                            print(f"\nYou used {spell["name"]} and healed {amount_to_add} HP!")
                            if player.current_hp > player.max_hp:
                                print("\nYou are now max HP!")
                                player.current_hp = player.max_hp
                            print(f"\nPlayer Health is now {player.current_hp}!\n")
                        elif spell["type"] == "attack":
                            damage = spell["amount"]
                            enemy.current_health -= damage
                            enemy.current_health = round(enemy.current_health, 1)
                            print(f"\nYou used {spell["name"]} against {enemy.name} and dealt {damage} damage!")
                            print(f"{enemy.name} HEALTH: {enemy.current_health}\n")
                            
                    elif choice == "4":
                        print(f"\nYou ran away from {enemy.name}!")
                        time.sleep(2.5)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        gameloop = False
                        fighting = False
                        stop = True
                        break

                    elif choice == "3":
                        print("ITEMS HERE")
                    
                    else:
                        print(f"Sorry, {choice} is not one of the available options! Please pick again!")
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
