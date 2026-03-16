import random as r

from enemy_class import *
from player_class import *

from player_inventory import *

class Effect:
    def __init__(self):

        self.on_fire = False
        self.electric = False

        self.stunned = False

        self.leeched = False

        self.dmg_down = False
        self.const_down = False
        self.charisma_down = False
        self.intelligence_down = False
        
    def onFireEffect(self, how_long, amount, applied):
        pass

    def electricEffect(self, how_long, amount, applied):
        pass
    
    def stunnedEffect(self, how_long, amount, applied):
        pass
    
    def leechedEffect(self, how_long, amount, applied):
        pass
    
    def dmgDown(self, how_long, amount, applied):
        pass
    
    def constDown(self, how_long, amount, applied):
        pass
    
    def charismaDown(self, how_long, amount, applied):
        pass

    def intelligenceDown(self, how_long, amount, applied):
        pass
