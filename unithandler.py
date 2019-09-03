from random import *
from dice import *


class Soldier:
	def __init__(self, name, description, rank, soldierrole, hp, maxhp, status, stamina, lifestate, mood, turnsenlisted):
		self.name = name
		self.description = description
		self.soldierrole = role
		self.hp = 10
		self.maxhp = 10
		#awaitingorder = idley awaiting for orders, marching = moving in formation, doubletime = marching faster 1.5x, breakrun = break formation and run to target reform = attempting to get in unit formation, engaged = currently locked in combat situation, routing = retreat scattering away, pursuing = moving after target 
		self.status = "awaitingorder"
		self.stamina = 100
		# 1 : alive/unscathed, 2 lightly wounded, 3 severely injured, 4 dying, 0 dead
		self.lifestate = 1
		self.mood = "content"
		self.turnsenlisted = 0
		self.rank = "private"
		self.tempEffect = " "
		
	def lifestateChk(self):
		if self.hp < (0.6666 * self.maxhp):
			self.lifestate = 2
		elif self.hp < (0.3333 * self.maxhp):
			self.lifestate = 3
		elif self.hp < (0.15 * self.maxhp):
			self.lifestate = 4
		elif self.hp <= 0:
			self.lifestate = 0
		else:
			pass
	def nerveChk(self):
		rollnerve = dice.Dice(20)
		nervesave = (self.discipline + self.morale)/2
		
		if rollnerve < nervesave:
			if self.nerve <= -3:
				self.mood = "hesitant"
				
				
			
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
		super().__init__(name, description, rank, soldierrole = "Infantry(Melee)", hp, maxhp, status, stamina, lifestate, mood, turnsenlisted)
		
class RangedInfantry(Soldier):
	def __init__(self, unitstyle, discipline, firingrate, atkRange, atkAccuracy, defense, mobility, awareness, morale, nerve, traits):
		#bowman, crossbowmen, thrown
		self.unitstyle = ""
		self.discipline = 10
		self.firingrate = 3 
		self.atkRange = 10
		self.atkAccuracy = 10
		self.defense = 10
		self.mobility = 10
		self.awareness = 10
		self.morale = 10	
		self.nerve = 0
		self.traits = {"eager recruit"}
		super().__init__(name, description, rank, soldierrole = "Infantry(Range)", hp, maxhp, status, stamina, lifestate, mood, turnsenlisted)
		
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
		super().__init__(name, description, rank, soldierrole = "Cavalry(Melee)", hp, maxhp, status, stamina, lifestate, mood, turnsenlisted)
		
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
		super().__init__(name, description, rank, soldierrole = "Cavalry(Ranged)", hp, maxhp, status, stamina, lifestate, mood, turnsenlisted)
	
#Melee INfantry types
class Peasant(MeleeInfantry):
	def __init__(self, weapon, unitID, cellID, armor, hitdie):
		self.weapon = "pitchfork"
		
		self.unitID = "lightinfantry" + (peasantsNum + 1)
		self.armor = "leather"
		self.hitdie = dice.Dice(4)
		super().__init__(name = "Peasant", description = "A low class citizen or farmer turned army fodder. They are weak and unorganized. They can be useful when unleashed in large formations and while not very effective on their own they can quickly overrun trained troops in mass.", rank, soldierrole = "Infantry(Melee)", hp, maxhp, status, stamina, lifestate, mood, turnsenlisted, unitstyle = "Peasant Melee", Discipline, charge, attack, defense, mobility, awareness, morale, nerve, traits)
		
	 
	def initStats(self):
		discMod = random.randint(-3, 1)
		chargeMod = random.randint(0, 3)
		attackMod = random.randint(0, 2)
		defenseMod = random.randint(0, 4)
		mobilityMod = random.randint(-2, 3)
		awarenessMod = random.randint(-3, 0)
		moraleMod = random.randint(-4, 1)
		
		self.discipline += discMod
		self.charge += chargeMod
		self.attack += attackMod
		self.defense += defenseMod
		self.mobility += mobilityMod
		self.awareness += awarenessMod
		self.morale += moraleMod
		
	def __str__(self):
		return "{}\n=====\n{}\nRank: {}\nUnitID: {}\nStatus: {}\nMood: {}\n Turns In Service: {}\nWeapon: {}\nArmor: {}\nAttack: {}\nDefense: {}\nCharge: {}\nDiscipline: {}\nMobility: {}\nAwareness: {}\nMorale: {}\nNerve: {}\nTraits: {}\n".format(self.unitstyle, self.description, self.unitID, self.status, self.mood, self.turnsenlisted, self.weapon, self.armor, self.attack, self.defense, self.charge, self.Discipline, self.Mobility, self.awareness, self.morale, self.nerve, self.traits)
		
	def takeDamage(self, damage):
		self.hp -= damage
		self.nerve -= 2
		self.mood = "shaken"
		self.morale -= dice.Dice(4)
		
		

		
class SpearmanMilitia(MeleeInfantry):
	def __init__(self, weapon, unitID, cellID, armor, weapondamage):
		self.weapon = "spear"
		self.unitID = "spearmanmilitia" + (spearNum + 1)
		self.armor = "leather"
		self.hitdie = dice.Dice(6)
		super().__init__(name = "Spearman Militia", description = "A militarized civilian with minimal gear and wielding a spear. They aren't very effective in charges and other offensive strategies, but can form defensive lines that are very effective against cavalry", rank, soldierrole = "Infanty (Ranged)", hp, maxhp, status, stamina, lifestate, mood, turnsenlisted, unitstyle = "Militia Spearman", discipline, charge, attack, defense, mobility, awareness, morale, nerve, traits)
		
	def initstats(self):
		discMod = random.randint(-2, 1)
		chargeMod = random.randint(-4, 0)
		attackMod = random.randint(-1, 1)
		defenseMod = random.randint(1, 3)
		mobilityMod = random.randint(-2, 2)
		awarenessMod = random.randint(-3, 0)
		moraleMod = random.randint(-3, 2)
		
		self.discipline += discMod
		self.charge += chargeMod
		self.attack += attackMod
		self.defense += defenseMod
		self.mobility += mobilityMod
		self.awareness += awarenessMod
		self.morale += moraleMod

	
	def __str__(self):
		return "{}\n=====\n{}\nRank: {}\nUnitID: {}\nStatus: {}\nMood: {}\nTurns In Service: {}\nWeapon: {}\nArmor: {}\nAttack: {}\nDefense: {}\nCharge: {}\nDiscipline: {}\nMobility: {}\nAwareness: {}\nMorale: {}\nNerve: {}\nTraits: {}\n".format(self.unitstyle, self.description, self.UnitId, self.status, self.mood, self.turnsenlisted, self.weapon, self.armor, self.attack, self.defense, self.charge, self.discipline, self.mobility, self.awareness, self.morale, self.nerve, self.traits)

class PeasantArcher(RangedInfantry):
	def __init__(self, weapon, unitID, cellID, armor, hitdie, ammunition):
		self.weapon = "longbow"
		self.unitID = "rangedunit" + (archersNum + 1)
		self.armor = "none"
		self.hitdie = dice.Dice(6)
		self.ammunition = 20
		super().__init__(name = "Peasant Archer", description = "A low class citizen or farmer turned army fodder. They are weak and unorganized. Their archers are usually self-trained and bad at executing complex strategies, but in large number can quickly deliver volleys of somewhat effective arrows", rank, soldierrole = "Infantry(Ranged)", hp, maxhp, status, stamina, lifestate, mood, turnsenlisted, unitstyle = "Peasant Ranged", firingrate, discipline, atkRange, mobility, awareness, morale, nerve, traits)
		
	def initstats(self):
		discMod = random.randint(-3, 1)
		rangeMod = random.randint(1, 3)
		accuracyMod = random.randint(0, 2)
		defenseMod = random.randint(-2, 0)
		mobilityMod = random.randint(0, 3)
		awarenessMod = random.randint(0, 3)
		moraleMod = random.randint(-3, 1)
		
		self.discipline += discMod
		self.atkRange += rangeMod
		self.atkAccuracy += accuracyMod
		self.defense += defenseMod
		self.mobility += mobilityMod
		self.awareness += awarenessMod
		self.morale += moraleMod
		self.firingrate = 3
		
