import random as r

from enemy_class import *
from player_class import *

from player_inventory import *

class Effect:
    def __init__(self, amount):
        self.amount = amount

        self.on_fire = False
        self.electric = False

        self.stunned = False

        self.leeched = False

        self.dmg_down = False
        self.const_down = False
        self.charisma_down = False
        self.intelligence_down = False
        
