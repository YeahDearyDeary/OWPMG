import random


class weapon_maker:
    def __init__ (self, name, item_type, weapon_type, mindamage,maxdamage, weapon_affinity, damage_type):
        
        self.name = name
        self.mindamage = mindamage
        self.maxdamage = maxdamage
        self.item_type = item_type 
        self.weapon_type = weapon_type
        self.weapon_affinity = weapon_affinity
        self.damage_type = damage_type
        
        
class suit_maker:
    def __init__ (self, name, item_type, redres, redstgres, whiteres, whitestgres, blackres, blackstgres, paleres, slres, slstgres, pires, pistgres, blres, blstgres):
        
        self.name = name
        self.item_type = item_type
        self.redres = redres
        self.redstgres = redstgres
        self.whiteres = whiteres
        self.whitestgres = whitestgres
        self.blackres = blackres
        self.blackstgres = blackstgres
        self.paleres = paleres
        self.slres = slres
        self.slstgres = slstgres
        self.pires = pires
        self.pistgres = pistgres
        self.blres = blres
        self.blstgres = blstgres

regsuit = suit_maker("Tattered Clothes", "Armor", 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 1.5, 1.5)
baton = weapon_maker("Standard Issue Baton", "Weapon", "Melee", 1, 2, "Blunt", "Red" )

full_item_list = ["Standard Issue Baton", "Tattered Clothes"]

def weaponnamegenerator(affinity):
    prefix = ["Million ", "Envyfull ", "Destructive ", "Explosive ", "Dangerous ", "Rumbling ", "Wrathfull ", "Pridefull ", "Glunttenous ", "Gloomy ", "Lustfull ", "Slothfull "]
    middle = [""]
    endstab = ["Spear", "Shiv", "Javilen", "Pole", "Dagger", "Sword", "Glaive", "Stilleto", "Pike"]
    endslash = ["Axe", "Dagger", "Sword", "Glaive", "Kopesh", "Schimitar", "Spear", "Javilen", "Short Sword", "Shiv", "Pike"]
    endblunt = ["Hammer", "Mace", "Pole", "Mallet", "Flail", "Brass Knuckles", "Shovel"]
    prefixchance = .3
    
    prefixname = ""
    middlename = ""
    endname = ""
    weaponname = None
    if random.random() < prefixchance:
        prefixname = random.choice(prefix)
    
    if affinity == "Slash":
        endname = random.choice(endslash)
    if affinity == "Blunt":
        endname = random.choice(endblunt)
    if affinity == "Pierce":
        endname = random.choice(endstab)
    
    if middlename == "":
        weaponname = prefixname + endname
    else:
        weaponname = prefixname + middlename + endname
    
    return weaponname

def suitnamegenerator():
    prefix = []
    middle = []
    end = ["Jacket", ""]
    prefixchance = .3
    
    prefixname = ""
    middlename = ""
    endname = ""
    suitname = None



def reeniweapons():
    weaponaffinitys = ["Slash", "Blunt", "Pierce"]
    weapon_affinity = random.choice(weaponaffinitys)
    name = weaponnamegenerator(weapon_affinity)
    mindamage = random.randint(1,3)
    maxdamage = random.randint(3,6)
    itemtype = "Weapon"
    weapontype = "Melee"
    damagetype = "Red"
    weapon = weapon_maker(name, itemtype, weapontype, mindamage, maxdamage, weapon_affinity, damagetype)
    return weapon
        
def reenisuits():
    name = suitnamegenerator()
    slashres = random.uniform(1.0, 2)
    slashstgres = random.uniform(1.0, 2)
    pierceres = random.uniform(1.0, 2)
    piercestgres = random.uniform(1.0, 2)
    bluntres = random.uniform(1.0, 2)
    bluntstgres = random.uniform(1.0, 2)
    redres = random.uniform(1.5, 2)
    redstgres = random.uniform(1.5, 2)
    whiteres = random.uniform(1.5, 2)
    whitestgres = random.uniform(1.5, 2)
    blackres = random.uniform(1.5, 2)
    blackstgres = random.uniform(1.5, 2)
    paleres = random.uniform(1.8, 2)
    suit = suit_maker()
    
    
def weapon_display(shop):
    if shop == "Reeniw":
        reeniweapon = reeniweapons()
        print(f"{reeniweapon.name}")
        print(f"Weapon Type: {reeniweapon.weapon_type}")
        print(f"Damage Type: {reeniweapon.damage_type}")
        print(f"Weapon Affinity: {reeniweapon.weapon_affinity}")
        print(f"Damage: {reeniweapon.mindamage} - {reeniweapon.maxdamage}")
        print()
        return reeniweapon
        
        
