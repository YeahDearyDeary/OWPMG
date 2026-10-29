import character
import entities
import items
import city
import math
import random

ahn = 1000
areas = city.areas
current_area = "J Corp Alleyways"
days = 1
actions = 5

# Set up the player real quick
player = character.player
player.suitslot = items.regsuit
player.suit_equip()

# Relationships

reeniworkshoprel = 0
chiyohazardsrel = 0
relationships = []
relationships.append("Chiyo's Hazard's")
relationships.append("Reeni's Workshop")

# Have combat slots for later
team1slot1 = None
team1slot2 = None
team1slot3 = None
team1slot4 = None
team1slot5 = None
team1backup = {}

team2slot1 = None
team2slot2 = None
team2slot3 = None
team2slot4 = None
team2slot5 = None
team2backup = {}

# Set Up Functions
def showday():
     print(f"It is Day: {days}")
     

def showplayerstats():
    pweapon1 = player.weapon1
    pweapon2 = player.weapon2
    psuit = player.suitslot
    print(f"Name: {player.name}")
    print()
    print("Status")
    print(f"Health: {player.health}/{player.maxhealth:.0f}")
    print(f"Sanity: {player.sanity}/{player.maxsanity:.0f}")
    print(f"Stagger: {player.stagger}/{player.maxstagger:.0f}")
    print(f"Status Effects: {player.statuses}")
    print()
    print("Stats")
    print(f"Fortitude: {player.fortitude}")
    print(f"Prudence: {player.prudence}")
    print(f"Temperence: {player.temperence}")
    print(f"Justice: {player.justice}")
    print()
    print("Combat Stats")
    print(f"Level: {player.level}")
    print(f"Offensive Level: {player.offensive_level}")
    print(f"Defensive Level: {player.defensive_level}")
    print(f"Reactions: {player.maxreactions}")
    print(f"Attack: {player.atk}")
    print(f"Attack Speed: {player.atkspeed}")
    print(f"Speed: {player.minspeed:.0f} - {player.maxspeed:.0f}")
    print(f"Work Ethinc: {player.workgain}")
    print(f"Work Speed: {player.workspeed}")
    print()
    print("Resistances")
    print(f"Slash Resistance: {player.slashres} | Pierce Resistance: {player.pierceres} | Blunt Resistance: {player.bluntres}")
    print(f"Slash Stagger Resistance: {player.slashstgres} | Pierce Stagger Resistance: {player.piercestgres} | Blunt Stagger Resistance: {player.bluntstgres}")
    print(f"Red Resistance: {player.redres} | Red Stagger Resistance {player.redstgres}")
    print(f"White Resistance: {player.whiteres} | White Stagger Resistance {player.whitestgres}")
    print(f"Black Resistance: {player.blackres} | Black Stagger Resistance {player.blackstgres}")
    print(f"Pale Resistance: {player.paleres}")
    print(f"Wrath Resistance: {player.wrathres} | Lust Resistance: {player.lustres}")
    print(f"Sloth Resistance: {player.slothres} | Gluttony Resistance: {player.gluttonyres}")
    print(f"Gloom Resistance: {player.gloomres} | Pride Resistance: {player.prideres}")
    print(f"Envy Resistance: {player.envyres}")
    print()
    print("Items and Equipment")
    print(f"Inventory: {player.inventory}")
    if player.weapon1 != None:
        print(f"Weapon Slot 1: {pweapon1.name}")
    else:
        print(f"Weapon Slot 1: {player.weapon1}")
    if player.weapon2 != None:
            print(f"Weapon Slot 2: {pweapon2.name}")
    else:
            print(f"Weapon Slot 2: {player.weapon2}")
    if player.suitslot != None:
        print(f"Suit Slot: {psuit.name}")
    else:
        print(f"Suit Slot: {player.suitslot}")
    print(f"Ego Gifts: {player.gifts}")
    
    
def add_to_combat(team, entity):
    global team1slot1
    global team1slot2 
    global team1slot3
    global team1slot4 
    global team1slot5

    global team2slot1 
    global team2slot2 
    global team2slot3 
    global team2slot4 
    global team2slot5 
    
    new_member = entity
    
    if team == 1:
        if team1slot1 == None:
            team1slot1 = new_member
        elif team1slot2 == None:
            team1slot2 = new_member
        elif team1slot3 == None:
            team1slot3 = new_member
        elif team1slot4 == None:
            team1slot4 = new_member
        elif team1slot5 == None:
            team1slot5 = new_member
        else:
            print("Team 1 Full")
            
    if team == 2:
        if team2slot1 == None:
            team2slot1 = new_member
        elif team2slot2 == None:
            team2slot2 = new_member
        elif team2slot3 == None:
            team2slot3 = new_member
        elif team2slot4 == None:
            team2slot4 = new_member
        elif team2slot5 == None:
            team2slot5 = new_member
        else:
            print("Team 2 Full")
        
add_to_combat(1, player)


def take_damage(entity, damage, type, affinity, sin):
    health = entity.health
    stagger = entity.stagger
    sanity = entity.sanity
    currenthealth = entity.health
    currentstagger = entity.stagger
    currentsanity = entity.sanity
    maxhealth = entity.maxhealth
    maxstagger = entity.maxstagger
    maxsanity = entity.maxsanity
    staggered = entity.staggered
    staggeredx2 = entity.staggeredx2
    staggeredx3 = entity.staggeredx3

    
    dmgmod = 0.0
    stgdmgmod = 0.0
    typedmgmod = 0.0
    typestgdmgmod = 0.0
    sindmgmod = None
    finalmod = None
    finalstgmod = None
    typedmg = None
    
    if affinity == "Slash":
        dmgmod = (dmgmod + entity.slashres)
        stgdmgmod = (stgdmgmod + entity.slashstgres)
        
    if affinity == "Blunt":
            dmgmod = (dmgmod + entity.bluntres)
            stgdmgmod = (stgdmgmod + entity.bluntstgres)
            
    if affinity == "Pierce":
            dmgmod = (dmgmod + entity.pierceres)
            stgdmgmod = (stgdmgmod + entity.piercestgres)
            
    if type == "Red":
        typedmgmod = (typedmgmod + entity.redres)
        typestgdmgmod = (typestgdmgmod + entity.redstgres)
        
    if type == "White":
            typedmgmod = (typedmgmod + entity.whiteres)
            
    if type == "Black":
        typedmgmod = (typedmgmod + entity.whiteres)
        typestgdmgmod = (typestgdmgmod  + entity.blackres)
        
    if type == "Pale":
        typedmgmod = (typedmgmod + entity.paleres)
        
        
    if sin != "None":
        # Put all the sin res here when ready deary
        
        if sindmgmod <= 0.0:
            finalmod = ((dmgmod - 1) + (typedmgmod - 1) + (-0.5))
            finalstgmod = ((stgdmgmod - 1) + (typestgdmgmod - 1))
        elif sindmgmod <= .9:
            finalmod = ((dmgmod - 1) + (typedmgmod - 1) + ((sindmgmod - 1)/2))
        elif sindmgmod >= 1.0:
            finalmod = ((dmgmod - 1) + (typedmgmod - 1) + (sindmgmod - 1))
        
    if sin == "None":
        if not any([staggered, staggeredx2, staggeredx3]):
            finalmod = ((dmgmod - 1) + (typedmgmod - 1))
            finalstgmod = ((stgdmgmod - 1) + (typestgdmgmod - 1))
        if staggered == True:
            finalmod = ((2) + (2))
            finalstgmod = ((2) + (2))
        if staggeredx2 == True:
            finalmod = ((2.5) + (2.5))
            finalstgmod = ((2.5) + (2.5))
        if staggeredx3 == True:
            finalmod = ((3) + (3))
            finalstgmod = ((3) + (3))
    
    if type == "Red":
        if finalmod != 0.0:
            noheal = health
            health = (health - ((damage * finalmod)))
            if health > noheal:
                health = noheal
            print(f"{entity.name} takes {damage * finalmod} Red damage")
            entity.health = health
        else:
            health = (health - (damage))
            print(f"{entity.name} takes {damage} Red damage")
            entity.health = health
        
        if finalstgmod != 0.0:
            nostaggerheal = stagger
            stagger = (stagger - ((damage * finalstgmod)))
            if stagger > nostaggerheal:
                stagger = nostaggerheal
            print(f"{entity.name} takes {damage * finalstgmod} Red stagger damage")
            entity.stagger = stagger
        else:
            stagger = (stagger - (damage))
            print(f"{entity.name} takes {damage * finalstgmod} Red stagger damage")
            entity.stagger = stagger

    # Stagger Systems
    if stagger <= 0 and staggered == False:
        print(f"{entity.name} gets staggered.")
        entity.staggered = True
        
    
    if stagger <= maxstagger * -.5 and staggered == True and staggeredx2 == False:
        print(f"{entity.name} is staggered+!")
        entity.staggeredx2 = True
    
    if stagger <= maxstagger * -1 and staggeredx2 == True and staggeredx3 == False:
        print(f"{entity.name} is staggered++!")
        entity.staggeredx3 = True
    

    if health <= 0:
        print(f"{entity.name} has been killed.")
        entity.health = 0
        return
    
    if health < currenthealth:
        print(f"{entity.name}'s Health: {health}/{maxhealth}")
    
    if stagger < currentstagger:
        print(f"{entity.name}'s Stagger: {stagger}/{maxstagger}")
    
    if sanity < currentsanity:
        print(f"{entity.name}'s Sanity: {sanity}/{maxsanity}")
    
    input()
    

def h2hreaction_turn(target, damage, type, affinity, sin, attacker):
    if target.health <= 0:
        print(f"{target.name} is dead")
        return

    
    if any([target.staggered, target.staggeredx2, target.staggeredx3]):
        print(f"{target.name} is staggered and cannot react.")
        take_damage(target, damage, type, affinity, sin)
        return

    if target.reactions <= 0:
        print(f"{target.name} has no reactions left.")
        take_damage(target, damage, type, affinity, sin)
        return
    
    if target.reactions > 0:
        target.reactions -= 1

    defenseaction = ['block', 'parry', 'riposte', 'counter', 'redirect', 'clash', 'dodge']
    defenseweight = [5, 3, 0, 2, 0, 0, 3]
    chosenaction = random.choices(defenseaction, weights=defenseweight, k=1)[0]
    
    if chosenaction == 'block':
        # default chance to block fully, changed with offense and defensive level, if not fully blocked partially blocked
        baseblockchance = .4
        offensivelevel = attacker.offensive_level
        defensivelevel = target.defensive_level
        levelmod = ((defensivelevel - offensivelevel) / 30)
        blockchance = 0.0
        blockreduction = -0.2
        levelreduction = (((offensivelevel - defensivelevel) /  100) - 0.1)
        
        blockchance = (baseblockchance + levelmod)
        
        if random.random() < blockchance:
            print(f"{target.name} blocks the attack.")
            input()
        else:
            print(f"{target.name} shoulders the damage.")
            input()
            damage = (damage + (blockreduction + levelreduction))
            take_damage(target, damage, type, affinity, sin)
            
    elif chosenaction == 'parry':
        # default change to parry the attack decreasing enemiies stagger and harming some depending on circumstances
        baseparrychance = .3
        offensivelevel = attacker.offensive_level
        defensivelevel = target.defensive_level
        levelmod = ((defensivelevel - offensivelevel) / 40)
        parrychance = 0.0
        
        parrychance = (baseparrychance + levelmod)
        
        if random.random() < parrychance:
            print(f"{target.name} parries the attack dealing {damage} stagger damage to {attacker.name}.")
            attacker.stagger = (attacker.stagger - damage)
            if attacker.stagger <= 0.0:
                print(f"{attacker.name} is staggered.")
                attacker.staggered = True
            input()
        else:
            print(f"{target.name} fails to parry the attack.")
            take_damage(target, damage, type, affinity, sin)
            
            
        
    elif chosenaction == 'clash':
        # chances to clash and win, clash for multiple turns, each time multiplying damage taken
        print()
    elif chosenaction == 'counter':
        # take the damage to hit freely yourself
        take_damage(target, damage, type, affinity, sin)
        
        
        if target.health <= 0.0:
            return
        if target.stagger <= 0.0:
            return
        
        
        weapon1 = None
        weapon2 = None
        weapon1dmg = None
        weapon2dmg = None
        if target.weapon1 != None:
            weapon1 = target.weapon1
            weapon1dmg = random.randint(weapon1.mindamage, weapon1.maxdamage)
            
                
                
        if target.weapon2 != None:
            weapon2 = target.weapon2
            weapon2dmg = random.randint(weapon2.mindamage, weapon2.maxdamage)
            
                
                
        if weapon1 == None:
            print(f"{target.name} punches {attacker.name} in retaliation.")
            input()
            take_damage(attacker, 1, "Red", "Blunt", "None")
        else:
            print(f"{target.name} attacks {attacker.name} in retaliation.")
            input()
            take_damage(attacker, weapon1dmg, weapon1.damage_type, weapon1.weapon_affinity, "None")
            
                    
        if weapon2 == None:
            print()
        else:
            print(f"{target.name} attacks {attacker.name} in retaliation.")
            take_damage(attacker, weapon2dmg, weapon2.damage_type, weapon2.weapon_affinity, "None")
            
    elif chosenaction == 'redirect':
        # high skill ceiling to make attacker hit enemy team memeber or team member
        print()
    elif chosenaction == 'riposte':
        # high skill ceiling to make the enemy lose their weapon causing them to have to pick it back up
        print()
    elif chosenaction == 'dodge':
        dodgechance = 0.0
        offensivelevel = attacker.offensive_level
        defensivelevel = target.defensive_level
        levelmod = ((defensivelevel - offensivelevel) / 30)
        basedodgechance = .3
        dodgechance = (basedodgechance + levelmod)
        
        if random.random() < dodgechance:
            print(f"{target.name} dodges the attack.")
            target.stagger = (target.stagger + damage)
            if target.stagger > target.maxstagger:
                target.stagger = target.maxstagger
            print(f"{target.name} gains {damage} stagger from the dodge.")
            input()
        else:
            print(f"{target.name} tries to dodge the attack.")
            print(f"{target.name} is hit by the attack.")
            input()
            take_damage(target, damage, type, affinity, sin)



def take_turn(entity):
    staggered = entity.staggered
    staggeredx2 = entity.staggeredx2
    staggeredx3 = entity.staggeredx3

    if entity.health <= 0:
        print(f"{entity.name} is dead.")
        return

    if entity.staggertimer >= 1:
            print(f"{entity.name} recovers from stagger.")
            entity.staggered = False
            entity.staggeredx2 = False
            entity.staggeredx3 = False
            entity.stagger = entity.maxstagger
            entity.staggertimer = 0

    if any([staggered, staggeredx2, staggeredx3]):
        if entity.staggertimer == 0:
            print(f"{entity.name} is staggered and cannot take their turn.")
        entity.staggertimer += 1
        return

    print(f"{entity.name} takes their turn.")
    input("Press Enter to continue")

    team1 = []
    team2 = []
    target = None
    
    if entity in (team1slot1, team1slot2, team1slot3, team1slot4, team1slot5):
        team2.extend([v for v in (team2slot1, team2slot2, team2slot3, team2slot4, team2slot5) if v is not None])
        target = random.choice(team2)
        
    if entity in (team2slot1, team2slot2, team2slot3, team2slot4, team2slot5):
            team1.extend([v for v in (team1slot1, team1slot2, team1slot3, team1slot4, team1slot5) if v is not None])
            target = random.choice(team1)
        
        
        
    
    
    entityactions = ['h2h', 'skill', 'page' ]
    actionweights = [10, 0, 0]
    chosenaction = random.choices(entityactions, weights=actionweights, k=1)[0]
    if chosenaction == 'h2h':
        weapon1 = None
        weapon2 = None
        weapon1dmg = None
        weapon2dmg = None
        
        
       
        if entity.weapon1 != None:
            weapon1 = entity.weapon1
            weapon1dmg = random.randint(weapon1.mindamage, weapon1.maxdamage)
            
            
        
        
        if entity.weapon2 != None:
            weapon2 = entity.weapon2
            weapon2dmg = random.randint(weapon2.mindamage, weapon2.maxdamage)
            
        
        
        
        if weapon1 == None:
            print(f"{entity.name} throws a punch at {target.name}.")
            h2hreaction_turn(target, 1, "Red", "Blunt", "None", entity)
            
        else:
            print(f"{entity.name} attacks {target.name} with their {weapon1.name}.")
            h2hreaction_turn(target, weapon1dmg, weapon1.damage_type, weapon1.weapon_affinity, "None", entity)
            
        if weapon2 == None:
            print()
        else:
            print(f"{entity.name} attacks {target.name} with their {weapon2.name}.")
            h2hreaction_turn(target, weapon2dmg, weapon2.damage_type, weapon2.weapon_affinity, "None", entity)
        
    elif chosenaction == 'skill':
        print()
    elif chosenaction == 'page':
        print()
    

    
def start_combat():
    turn_order = []

    global team1slot1
    global team1slot2 
    global team1slot3
    global team1slot4 
    global team1slot5

    global team2slot1 
    global team2slot2 
    global team2slot3 
    global team2slot4 
    global team2slot5

    if team1slot1 != None:
        team1slot1.reactions = team1slot1.maxreactions
        speed = random.randint(team1slot1.minspeed, team1slot1.maxspeed)
        turn_order.append((speed, team1slot1))
    
    if team1slot2 != None:
        team1slot2.reactions = team1slot2.maxreactions
        speed = random.randint(team1slot2.minspeed, team1slot2.maxspeed)
        turn_order.append((speed, team1slot2))
    
    if team1slot3 != None:
        team1slot3.reactions = team1slot3.maxreactions
        speed = random.randint(team1slot3.minspeed, team1slot3.maxspeed)
        turn_order.append((speed, team1slot3))
    
    if team1slot4 != None:
        team1slot4.reactions = team1slot4.maxreactions
        speed = random.randint(team1slot4.minspeed, team1slot4.maxspeed)
        turn_order.append((speed, team1slot4))
    
    if team1slot5 != None:
        team1slot5.reactions = team1slot5.maxreactions
        speed = random.randint(team1slot5.minspeed, team1slot5.maxspeed)
        turn_order.append((speed, team1slot5))
        
    if team2slot1 != None:
        team2slot1.reactions = team2slot1.maxreactions
        speed = random.randint(team2slot1.minspeed, team2slot1.maxspeed)
        turn_order.append((speed, team2slot1))
        
    if team2slot2 != None:
        team2slot2.reactions = team2slot2.maxreactions
        speed = random.randint(team2slot2.minspeed, team2slot2.maxspeed)
        turn_order.append((speed, team2slot2))
        
    if team2slot3 != None:
        team2slot3.reactions = team2slot3.maxreactions
        speed = random.randint(team2slot3.minspeed, team2slot3.maxspeed)
        turn_order.append((speed, team2slot3))
        
    if team2slot4 != None:
        team2slot4.reactions = team2slot4.maxreactions
        speed = random.randint(team2slot4.minspeed, team2slot4.maxspeed)
        turn_order.append((speed, team2slot4))
        
    if team2slot5 != None:
        team2slot5.reactions = team2slot5.maxreactions
        speed = random.randint(team2slot5.minspeed, team2slot5.maxspeed)
        turn_order.append((speed, team2slot5))
    
    for speed, entity in sorted(turn_order, key=lambda x: x[0], reverse=True):
        take_turn(entity)
        print("Next Turn")
        print()
    
def begin_encounter():
    print("An encounter has begun.")
    in_combat = True
    turns = 1
    global team1slot1
    global team1slot2 
    global team1slot3
    global team1slot4 
    global team1slot5

    global team2slot1 
    global team2slot2 
    global team2slot3 
    global team2slot4 
    global team2slot5

    while in_combat:

        if team1slot1 != None:
            if team1slot1.health <= 0:
                team1slot1 = None
        if team1slot2 != None:
            if team1slot2.health <= 0:
                team1slot2 = None
        if team1slot3 != None:
            if team1slot3.health <= 0:
                team1slot3 = None
        if team1slot4 != None:
            if team1slot4.health <= 0:
                team1slot4 = None
        if team1slot5 != None:
            if team1slot5.health <= 0:
                team1slot5 = None
        if team2slot1 != None:
            if team2slot1.health <= 0:
                team2slot1 = None
        if team2slot2 != None:
            if team2slot2.health <= 0:
                team2slot2 = None
        if team2slot3 != None:
            if team2slot3.health <= 0:
                team2slot3 = None
        if team2slot4 != None:
            if team2slot4.health <= 0:
                team2slot4 = None
        if team2slot5 != None:
            if team2slot5.health <= 0:
                team2slot5 = None

        print(f"Turn {turns}")

        if not any(v is not None for v in (team1slot1, team1slot2, team1slot3, team1slot4, team1slot5)):
            print("Everyone Has Fallen...")
            in_combat = False
            break
        if not any(v is not None for v in (team2slot1, team2slot2, team2slot3, team2slot4, team2slot5)):
            print("All Enemies Have Fallen...")
            in_combat = False
            break

        start_combat()
        turns += 1

def encounters():
    global current_area
    global ahn

    encounter_chance = 0.0
    encounterloop = False
    if current_area == "J Corp Alleyways":
        encounter_chance = 0.2
        if random.random() < encounter_chance:
            encounterloop = True
            print("Some shadowy figures approach you begging for your Ahn.")
            print(f"You have {ahn} Ahn.")
            print("What do you do?")
            print("1. Give them some money (200 Ahn)")
            print("2. Brush them off and keep walking")
            print("3. Run away as fast as possible")
            print("4. Threaten to rob them")
            print("5. Attack the one asking for money")
            print("6. Reason with them")
            print()
            while encounterloop:
                player_choice = input("Enter your choice: ")
                if player_choice == "1":
                    if ahn >= 200:
                        print()
                        print("You hand them some Ahn for their troubles.")
                        ahn -= 200
                        print(f"You have {ahn} Ahn left.")
                        input()
                        print("J Corp Waster: 'Heh, thanks for this, I can feel my luck changing already!")
                        print("They leave.")
                        input()
                        encounterloop = False
                        break
                    else:
                        attack_chance = 0.5
                        print("You don't have enough Ahn to give them.")
                        print("J Corp Waster: 'Damn it! I knew this jackass was broke!")
                        print()
                        input()
                        if random.random() < attack_chance:
                            print("J Corp Waster: 'Lets just take his organs! It'll sell for well")
                            print("They attack you!")
                            input()
                            waster1 = entities.jcorpwaster(1)
                            waster2 = entities.jcorpwaster(1)
                            waster3 = entities.jcorpwaster(1)
                            add_to_combat(2, waster1)
                            add_to_combat(2, waster2)
                            add_to_combat(2, waster3)
                            begin_encounter()
                            encounterloop = False
                            break
                        else:
                            print("J Corp Waster: 'What a load of Shite...")
                            print("They leave.")
                            input()
                            encounterloop = False
                            break
                elif player_choice == "2":
                    attack_chance = 0.7
                    print("Brushing the first figure's shoulder you keep walking.")
                    input()
                    if random.random() < attack_chance:
                        print("J Corp Waster: 'Hurry and grab em! We'll just take what we want!")
                        print("They attack you!")
                        input()
                        waster1 = entities.jcorpwaster(1)
                        waster2 = entities.jcorpwaster(1)
                        waster3 = entities.jcorpwaster(1)
                        add_to_combat(2, waster1)
                        add_to_combat(2, waster2)
                        add_to_combat(2, waster3)
                        begin_encounter()
                        encounterloop = False
                        break
                    else:
                        print("J Corp Waster: 'Asshole...")
                        print("They leave.")
                        input()
                        encounterloop = False
                        break
                elif player_choice == "3":
                    print("You bolt, avoiding any type of manipulation tactics they may employ")
                    input()
                    encounterloop = False
                    break
                else:
                    print("That is not an option.")
    
    
def actionchoice():
    global current_area
    global relationships
    if player.health <= 0:
        print()
        print("You have died.")
        print(f"Days Survived: {days}")
        print(f"Total Ahn Collected: {ahn}")
        print(f"Player Level {player.level}")
        return
    travel = {"1", "Travel", "travel", "T", "t"}
    interact = {"2", "Interact", "interact", "It", "it"}
    combatskills = {"3", "Combat Skills", "combat skills", "combat Skills", "Combat skills", "CS", "cs"}
    characterstatus = {"4", "Character Stats", "Character stats", "character Stats", "character stats", "CHS", "chs"}
    inventory = {"5", "Inventory", "inventory", "i", "I"}
    Team = {"6", "Team", "team", "Te", "te"}
    save = {"7", "Save", "save", "s", "S"}
    print(f"You have {actions} actions left")
    print(f"Current Area: {current_area}")
    print("\n" + areas[current_area]["description"])
    print("What do you do?")
    print("1. Travel")
    print("2. Interact")
    print("3. Combat Skills")
    print("4. Character Stats")
    print("5. Inventory")
    print("6. Team")
    print("7. Save")
    selected_action = input()
    if selected_action in travel:
        while True:
            print(areas[current_area]["exits"])
            choice = input("Where do you go? ('Stop' to go back.): ")
        
            if choice == "Stop":
                print("Going Back")
                break
            
            exits = areas[current_area]["exits"]
            numerical_choices = {str(i + 1): exit_name for i, exit_name in enumerate(exits)}
            if choice in numerical_choices:
                choice = numerical_choices[choice]
            if choice in exits:
                print(f"You go to {choice}")
                current_area = choice
                encounters()
                break
            else:
                print("Can't do that")
        actionchoice()
    elif selected_action in interact:
        if areas[current_area].get("interactable"):
            buy = ["Buy", "buy"]
            sell = ["Sell", "sell"]
            if areas[current_area] == "Reeni's Workhop":
                print(f"Reeni's Workshop Relationship: {reeniworkshoprel}")
                
                
            print(areas[current_area]["interactable"])
            print()
            
            while True:
                
                choice = input("What would you like to do?")
            
                if areas[current_area] == "Reeni's Workshop":
                    if choice in buy:
                        print()
                        
                        break
                    elif choice in sell:
                        print()
                        
                        break
                    elif choice == "Stop":
                        break
                    else:
                        print("That isn't an option")
        else:
            print("There's nothing to interact with here.")
        input()
        actionchoice()
    elif selected_action in combatskills:
        print()
        actionchoice()
    elif selected_action in characterstatus:
        showplayerstats()
        input()
        actionchoice()  
    elif selected_action in inventory:
        print()
        actionchoice()
    elif selected_action in Team:
        print("Team Members:")
        print(f"Slot 1: {team1slot1.name if team1slot1 is not None else 'Empty'}")
        print(f"Slot 2: {team1slot2.name if team1slot2 is not None else 'Empty'}")
        print(f"Slot 3: {team1slot3.name if team1slot3 is not None else 'Empty'}")
        print(f"Slot 4: {team1slot4.name if team1slot4 is not None else 'Empty'}")
        print(f"Slot 5: {team1slot5.name if team1slot5 is not None else 'Empty'}")
        input()
        actionchoice()
    elif selected_action in save:
        print()
        actionchoice()  
    else:
        print("That is not an option")
        actionchoice()

# Set up the game
def start_game():
    input("Press Enter to Continue. ")
    print("As you open your eyes you look around to see a few trash bins and huge crowding walls...")
    input()
    print("for whatever reason you've now found yourself stranded and alone in J Corp.")
    print("This new situation won't stop you from surviving in this unfair city...")
    input()
    # Change Players name from Player
    print("My name is...")
    player_name = input("Enter a Name: ")
    player.name = player_name
    print(f"This is the beginning of {player_name}'s Purgatory")
    input()
    showday()
    actionchoice()

start_game()







