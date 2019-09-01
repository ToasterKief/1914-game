class Units:
    def __init__(self, name, faction, category, maxForces. currentForce, status, stamina, location-x, location-y, alive = True):
        self.unitname = unitname
        self.faction = faction
        self.category = UnitCategory
        self.maxForces = 0
        self.currentForce = 0
        self.status = status
        self.stamina = 100
        self.location-x = (0)
        self.location-y = (0)
    def unitinfo(self):
        return "{}\n=====\n{}\nUnit Size: {}\nSurviving Troops: {}\nStatus: {}".format(self.unitname, self.category, self.maxForces, self.currentForce)
   
   
   ##Unit classes are infantry, armor, and support
   ##infantry: riflemen,
   ##artillery: mortarcrew, flakgun
   ##support: gunner, marksmen, scout
   #misc: mediccrew, comms, resupply
   
   #unit sizes
