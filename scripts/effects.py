import random as r

from enemy_class import *
from player_class import *

from player_inventory import *

class Effect:
    def __init__(self):
        
        self.effects = {
            'on_fire': {'active': False, 'applied': False},
            'electric': {'active': False, 'applied': False},
            'stunned': {'active': False, 'applied': False},
            'leeched': {'active': False, 'applied': False},
            'dmg_down': {'active': False, 'applied': False},
            'const_down': {'active': False, 'applied': False},
            'charisma_down': {'active': False, 'applied': False},
            'intelligence_down': {'active': False, 'applied': False},
        }
        
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
