class Soldier:
	def __init__(self, name, description, rank, soldierrole, hp, status, stamina, lifestate, mood, turnsenlisted):
		self.name = name
		self.description = description
		self.soldierrole = role
		self.hp = 10
		self.status = "idle"
		self.stamina = 100
		self.lifestate = "alive"
		self.mood = "content"
		self.turnsenlisted = 0
		self.rank = "private"
		
		
class MeleeInfantry(Soldier):
	def __init__(self, unitstyle, discipline, charge, attack, defense, mobility, awareness, morale, nerve, traits):
		#light infantry, heavy, spearmen
		self.unitstyle = ""
		self.discipline = 10
		self.charge = 10
		self.attack = 10
		self.defense = 10
		self.mobility = 10
		self.awareness = 10
		self.morale = 10
		self.nerve = 0
		self.traits = {eager recruit}
		super().__init__(name, description, rank, soldierrole = "Infantry(Melee)", hp, status, stamina, lifestate, mood, turnsenlisted)
		
class RangedInfantry(Soldier):
	def __init__(self, unitstyle, discipline, atkRange, atkAccuracy, defense, mobility, awareness, morale, nerve, traits):
		#bowman, crossbowmen, thrown
		self.unitstyle = ""
		self.discipline = 10
		self.atkRange = 10
		self.atkAccuracy = 10
		self.defense = 10
		self.mobility = 10
		self.awareness = 10
		self.morale = 10
		self.nerve = 0
		self.traits = {"eager recruit"}
		super().__init__(name, description, rank, soldierrole = "Infantry(Range)", hp, status, stamina, lifestate, mood, turnsenlisted)
		
class MeleeCavalry(Soldier):
	def __init__(self, unitstyle, discipline, mounted, charge, attack, defense, mobility, awareness, morale, nerve, traits):
		#Lancer/Spear, Swordsman, Ranged
		self.unitstyle = ""
		self.discipline = 10
		self.mounted = True
		self.charge = 10
		self.attack = 10
		self.defense = 10
		self.mobility = 10
		self.awareness = 10
		self.morale = 10
		self.nerve = 0
		self.traits = {"eager recruit", "horseman"}
		super().__init__(name, description, rank, soldierrole = "Cavalry(Melee)", hp, status, stamina, lifestate, mood, turnsenlisted)
		
class RangedCavalry(Soldier):
	def __init__(self, unitstyle, discipline, mounted, atkRange, atkAccuracy, defense, mobility, awareness, morale, nerve, traits):
		#crossbow, bowman, javelin
		self.unitstyle = ""
		self.discipline = 10
		self.mounted = True
		self.charge = 10
		self.attack = 10
		self.defense = 10
		self.mobility = 10
		self.awareness = 10
		self.morale = 10
		self.nerve = 0
		self.traits = {"eager recruit", "horseman"}
		super().__init__(name, description, rank, soldierrole = "Cavalry(Ranged)", hp, status, stamina, lifestate, mood, turnsenlisted)


		
#Melee INfantry types
class Peasant(MeleeInfantry):
	def __init__(self, weapon, unitID, cellID, armor, weapondamage):
		self.weapon = "pitchfork"
		self.cellID = "infantry" + (cellNum + 1)
		self.unitID = "lightinfantry" + (peasantsNum + 1)
		self.armor = "leather"
		self.weapondamage = 

			       
