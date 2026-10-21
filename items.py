
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

full_item_list = {"Standard Issue Baton", "Tattered Clothes"}
