import random
import items
import math

weaponcreate = items.weapon_maker
suitcreate = items.suit_maker


class OneSin:
    # Basic Properties
    name = "One Sin A Thousand Good Deeds"
    form = "Abnormality"
    level = 1
    # Base attributes
    health = (200.0 * (level *.2))
    # Work Properties
    maximum_boxes = 24
    default_work_chance = .60
    surplus_chance = .20 # Surplus is the chance to gain more boxes with the abno for free, doesn't hurt the employee
    surplus_amount = 6
    good_work_min = 18
    neutral_work_min = 9
    ego_weapon_cost = 30
    ego_suit_cost = 50
    
class jcorpwaster:
    def __init__ (self, level):
        self.name = "J Corp Waster"
        self.staggered = False
        self.staggeredx2 = False
        self.staggeredx3 = False
        self.staggertimer = 0
        self.maxreactions = 1
        self.reactions = self.maxreactions
        self.level = level
        self.offensive_level = level
        self.defensive_level = level
        self.health = (5 + (2 * level))
        self.stagger = (3 + (1 * level))
        self.sanity = (2 + (.5 * level))
        self.maxhealth = self.health
        self.maxstagger = self.stagger    
        self.maxsanity = self.sanity
        self.attackspeed = 1.0
        self.maxspeed = 4
        self.minspeed = 1
        self.slashres = 2.0
        self.slashstgres = 2.0
        self.pierceres = 2.0
        self.piercestgres = 2.0
        self.bluntres = 2.0
        self.bluntstgres = 2.0
        self.redres = 2.0
        self.redstgres = 2.0
        self.whiteres = 2.0
        self.whitestgres = 2.0
        self.blackres = 2.0
        self.blackstgres = 2.0
        self.paleres = 2.0
        self.statuses = []
        self.itempool = []
        randwep1, randwep2, randwep3 = weaponcreate("Rusty Pipe", "Weapon", "Melee", 1, 1, "Blunt", "Red"), weaponcreate("Glass Shiv", "Weapon", "Melee", 1, 1, "Slash", "Red"), weaponcreate("Sharp Rebarb", "Weapon", "Melee", 1, 1, "Pierce", "Red")
        randwep = [randwep1, randwep2, randwep3]
        self.weapon1 = random.choice(randwep)
        self.weapon2 = None
    
    

