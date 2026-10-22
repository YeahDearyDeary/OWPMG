import items
import math
import random

weaponcreate = items.weapon_maker
suitcreate = items.suit_maker

class player:
    #basic properties
    name = "Player"
    form = "Humanoid"
    staggered = False
    staggeredx2 = False
    staggeredx3 = False
    # Base Stats
    fortitude = 0.0
    prudence = 0.0
    temperence = 0.0
    justice = 0.0
    
    # Base Attributes
    level = 1
    offensive_level = 1
    defensive_level = 1
    health = (20.0 + (fortitude // .5))
    sanity = (10.0 + (prudence // .5))
    stagger = (10.0 + (fortitude // 1.5))
    mental = (10 + (prudence // 1.5))
    maxhealth = health
    maxsanity = sanity
    maxstagger = stagger
    atk = (0.0 + (offensive_level // 3))
    atkspeed = (1.0 + ((justice // 10) * .1))
    maxspeedequation = (5 + ((justice // .1)))
    minspeedequation = (1 + ((justice // .1)))
    maxspeed = int(maxspeedequation)
    minspeed = int(minspeedequation)
    workgain = (.1 + ((temperence // 1) * .2))
    workspeed = (.5 + ((temperence // 1) * .1))
    
    # Affinity Resistances
    slashres = 2.0
    slashstgres = 2.0
    pierceres = 2.0
    piercestgres = 2.0
    bluntres = 2.0
    bluntstgres = 2.0
    # Type Resistances
    redres = 2.0
    redstgres = 2.0
    whiteres = 2.0
    whitestgres = 2.0
    blackres = 2.0
    blackstgres = 2.0
    paleres = 2.0
    # Sin Resistances
    wrathres = 1.0
    lustres = 1.0
    slothres = 1.0
    gluttonyres = 1.0
    gloomres = 1.0
    prideres = 1.0
    envyres = 1.0
    
    
    # Inventory and Items
    inventory = []
    weapon1 = None
    weapon2 = None
    suitslot = None
    gifts = []
    
    # Status Effects
    statuses = []
    
    def damage_1():
        weapon1 = player.weapon1
        atk = player.atk
        type = None
        weaponatk = 0
        
        if weapon1 != None:
            type = weapon1.damage_type
            affinity = weapon1.weapon_affinity
            weaponatk = random.randint(weapon1.mindamage, weapon1.maxdamage)
            if weapon1.weapon_type == "Melee":
                print(f"{player.name} swings their {weapon1.name}")
            if weapon1.weapon_type == "Ranged":
                print(f"{player.name} raises their {weapon1.name}")
        else:
            print(f"{player.name} tries to punch")
            type = "Red"
        
        
        final_damage =  atk + weaponatk 
        return final_damage, type, affinity
    
    def damage_2():
        weapon2 = player.weapon2
        atk = player.atk
        
        if weapon2 != None:
            if weapon2.weapon_type == "Melee":
                print(f"{player.name} swings their {weapon2.name}")
            if weapon2.weapon_type == "Ranged":
                print(f"{player.name} raises their {weapon2.name}")
        type = weapon2.damage_type
        weaponatk = random.randint(weapon2.mindamage, weapon2.maxdamage)
        final_damage = atk + weaponatk
        return final_damage
    
    def suit_equip():
        suitslot = player.suitslot

        
        player.redres = suitslot.redres
        player.redstgres = suitslot.redstgres
        player.whiteres = suitslot.whiteres
        player.whitestgres = suitslot.whitestgres
        player.blackres = suitslot.blackres
        player.blackstgres = suitslot.blackstgres
        player.paleres = suitslot.paleres


        
            
        
            
        
        
    
    
    
    
    
    
    
    