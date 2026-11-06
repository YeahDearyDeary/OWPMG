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

regsuit = suit_maker("Tattered Clothes", "Armor", 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0)
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
    end = ["Jacket", "Sweater", "Coat", "Hoodie", "Button Up", "Sleeveless Suit", "Trench Coat", "Parka", "Overcoat", "Lowly Butler Suit", "Fixer Upper", "Puffy Vest",]
    prefixchance = .3
    
    prefixname = ""
    middlename = ""
    endname = ""
    suitname = None

    endname = random.choice(end)

    suitname = prefixname + middlename + endname
    return suitname



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
    itemtype = "Armor"
    slashres = round(random.uniform(1.0, 2.0), 1)
    slashstgres = round(random.uniform(1.0, 2.0), 1)
    pierceres = round(random.uniform(1.0, 2.0), 1)
    piercestgres = round(random.uniform(1.0, 2.0), 1)
    bluntres = round(random.uniform(1.0, 2.0), 1)
    bluntstgres = round(random.uniform(1.0, 2.0), 1)
    redres = round(random.uniform(1.5, 2.0), 1)
    redstgres = round(random.uniform(1.5, 2.0), 1)
    whiteres = round(random.uniform(1.5, 2.0), 1)
    whitestgres = round(random.uniform(1.5, 2.0), 1)
    blackres = round(random.uniform(1.5, 2.0), 1)
    blackstgres = round(random.uniform(1.5, 2.0), 1)
    paleres = round(random.uniform(1.8, 2.0), 1)
    suit = suit_maker(name, itemtype, slashres, slashstgres, pierceres, piercestgres, bluntres, bluntstgres, redres, redstgres, whiteres, whitestgres, blackres, blackstgres, paleres)
    
    return suit


def item_display(item):
    if item.item_type == "Weapon":
        reeniweapon = item
        print(f"{reeniweapon.name}")
        print(f"Weapon Type: {reeniweapon.weapon_type}")
        print(f"Damage Type: {reeniweapon.damage_type}")
        print(f"Weapon Affinity: {reeniweapon.weapon_affinity}")
        print(f"Damage: {reeniweapon.mindamage} - {reeniweapon.maxdamage}")
        print()
        return reeniweapon
    if item.item_type == "Armor":
        reenisuit = item
        print(f"{reenisuit.name}")
        print("Resistances - ")
        print(f"Slash Resistance: {reenisuit.slres} | Slash Stagger Resistance: {reenisuit.slstgres}")
        print(f"Pierce Resistance: {reenisuit.pires} | Pierce Stagger Resistance: {reenisuit.pistgres}")
        print(f"Blunt Resistance: {reenisuit.blres} | Blunt Stagger Resistance: {reenisuit.blstgres}")
        print("Type Resistances - ")
        print(f"Red Resistance: {reenisuit.redres} | Red Stagger Resistance: {reenisuit.redstgres}")
        print(f"White Resistance: {reenisuit.whiteres} | White Stagger Resistance: {reenisuit.whitestgres}")
        print(f"Black Resistance: {reenisuit.blackres} | Black Stagger Resistance: {reenisuit.blackstgres}")
        print(f"Pale Resistance: {reenisuit.paleres}")
        print()
        return reenisuit
        
def item_price(item):
    if isinstance(item, weapon_maker):
        price = 0
        if item.weapon_type == "Melee":
            price += random.randint(50, 200)
        elif item.weapon_type == "Ranged":
            price += random.randint(200, 500)
        if item.weapon_affinity == "Slash":
            price += random.randint(20, 100)
        elif item.weapon_affinity == "Blunt":
            price += random.randint(20, 100)
        elif item.weapon_affinity == "Pierce":
            price += random.randint(20, 100)
        if item.damage_type == "Red":
            price += random.randint(50, 200)
        elif item.damage_type == "White":
            price += random.randint(400, 600)
        elif item.damage_type == "Black":
            price += random.randint(800, 1200)
        elif item.damage_type == "Pale":
            price += random.randint(10000, 15000)
        if item.mindamage > 1:
            price += (item.mindamage - 1) * 20
        if item.maxdamage > 3:
            price += (item.maxdamage - 3) * 80
        

        
        return price
    if isinstance(item, suit_maker):
        price = 0
        if item.slres >= 1.0:
            price += 100
            price -= (item.slres - 1.0) * 100
        if item.slstgres >= 1.0:
            price += 100
            price -= (item.slstgres - 1.0) * 100
        if item.pires >= 1.0:
            price += 100
            price -= (item.pires - 1.0) * 100
        if item.pistgres >= 1.0:
            price += 100
            price -= (item.pistgres - 1.0) * 100
        if item.blres >= 1.0:
            price += 100
            price -= (item.blres - 1.0) * 100
        if item.blstgres >= 1.0:
            price += 100
            price -= (item.blstgres - 1.0) * 100
        if item.redres > 1.0:
            price += 100
            price -= (item.redres - 1.0) * 100
        if item.redstgres > 1.0:
            price += 100
            price -= (item.redstgres - 1.0) * 100
        if item.whiteres > 1.0:
            price += 100
            price -= (item.whiteres - 1.0) * 100
        if item.whitestgres > 1.0:
            price += 100
            price -= (item.whitestgres - 1.0) * 100
        if item.blackres > 1.0:
            price += 100
            price -= (item.blackres - 1.0) * 100
        if item.blackstgres > 1.0:
            price += 100
            price -= (item.blackstgres - 1.0) * 100
        if item.paleres > 1.0:
            price += 200
            price -= (item.paleres - 1.0) * 100
        
        return price
        

