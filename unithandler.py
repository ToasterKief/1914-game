from random import *
from dice import *


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
		
		self.unitID = "lightinfantry" + (peasantsNum + 1)
		self.armor = "leather"
		self.hitdie = dice.Dice(4)
		super().__init__(name = "Peasant", description = "A low class citizen or farmer turned army fodder. They are weak and unorganized. They can be useful when unleashed in large formations and while not very effective on their own they can quickly overrun trained troops in mass.", rank, soldierrole = "Infantry(Melee)", hp, status, stamina, lifestate, mood, turnsenlisted, unitstyle = "Peasant Melee", Discipline, charge, attack, defense, mobility, awareness, morale, nerve, traits)
		
		 
	def initStats(self):
		discMod = random.randint(-3, 1)
		chargeMod = random.randint(0, 3)
		attackMod = random.randint(0, 2)
		defenseMod = random.randint(0, 4)
		mobilityMod = random.randint(-2, 3)
		awarenessMod = random.randint(-5, 0)
		moraleMod = random.randint(=4, 1)
		
		self.Discipline += discMod
		self.charge += chargeMod
		self.attack += attackMod
		self.defense += defenseMod
		self.mobility += mobilityMod
		self.awareness += awarenessMod
		self.morale += moraleMod
		
	def __str__(self):
		return "{}\n=====\n{}\nRank: {}\nUnitID: {}\nStatus: {}\nMood: {}\n Turns In Service: {}\nWeapon: {}\nArmor: {}\nAttack: {}\nDefense: {}\nCharge: {}\nDiscipline: {}\nMobility: {}\nAwareness: {}\nMorale: {}\nNerve: {}\nTraits: {}\n".format(self.unitstyle, self.description, self.unitID, self.status, self.mood, self.turnsenlisted, self.weapon, self.armor, self.attack, self.defense, self.charge, self.Discipline, self.Mobility, self.awareness, self.morale, self.nerve, self.traits)
		
class SpearmanMilitia(MeleeInfantry):
	def __init__(self, weapon, unitID, cellID, armor, weapondamage):
		self.weapon = "spear"
		self.unitID = "spearmanmilitia" + (spearNum + 1)
		self.armor = "leather"
		self.hitdie = dice.Dice(6)
		super().__init__(name = "Spearman Militia", description = "A militarized civilian with minimal gear and wielding a spear. They aren't very effective in charges and other offensive strategies, but can form defensive lines 

	
