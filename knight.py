# knight.py
# Sarah Darrow
# sd1209
# 11/9/15
#
# The definition of the knight class 

from random import *

class Knight:
    def __init__ (self, name,  damage_high, damage_low):
        self.name = name
        self.damage_high = damage_high
        self.damage_low = damage_low
        self.health = 100
        self.rage = 0
        self.limbs = ["left arm", "right arm", "left leg", "right leg"]
    
    def crit(self):
        crit = [False]*100
        crit[0:self.rage] = [True]*self.rage
        return crit[randint(0, 99)]
        
    def attack(self, other):
        print(self.name, "attacks", other.name)
        
        hit = randint(self.damage_low, self.damage_high)
        if self.crit():
            self.rage = 0
            hit*=2
            print("Critical Attack!!")
        else:
            self.rage += 15
            if self.rage > 100:
                self.rage = 100
        
        other.health -= hit
        if(other.health < 0):
            other.health = 0
            
        other._updateLimbs()
        
    def _updateLimbs(self):
        if 100-self.health-(4-len(self.limbs))*25 >= 25:
            for each in range(0, (100-self.health-(4-len(self.limbs))*25)//25):
                if(len(self.limbs) != 0):
                    limbLost = self.limbs.pop(randint(0, len(self.limbs)-1))
                    print(self.name, "has lost his", limbLost)
        
    def hasLimbs(self):
        return len(self.limbs) > 0
    
    def __str__(self):
        return self.name+ ' '+str(self.health)+'hp \t'
    
    
            
        
        
    
    