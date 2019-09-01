

##The game runs on d20. Instead of using arbitrary randints, we will use the system dnd uses in which a 20 sided die can handle RNG for checking if actions are successful, spawn tables and random event initialization. THe standard dnd hit die are also effective for controlling RNG data regarding damage values

import random
import os


class Dice:
    def __init__(self, sides=1):
        self.sides = sides
        self.result = []
        self.total = 0
    
    def __roll(self):
        return random.randint(1, self.sides)
    def roll(self,times=1):
        self.result[:] = [self._roll() for time in range(times)]
        self.sum_result()
        
    def sum_result(self):
        self.total = sum(self.result)
        
    def save_result(self, directory=""):
        with open(os.path.join(directory, "savedroll.txt"), "a") as txt:
            txt.write(%d\n" % self.total
        
   
   
