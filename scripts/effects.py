import random as r

from enemy_class import *
from player_class import *

from player_inventory import *

from fighting_mechanics import *

class Effect:
    def __init__(self, effects_on_self: list, target, target_consum_inv, target_spell_inv):
        self.target = target
        self.target_consum_inv = target_consum_inv
        self.target_spell_inv = target_spell_inv

        self.effects_on_self = effects_on_self

        self.effects = {
            'on_fire': {'active': False, 'applied': False, 'func': {self.onFireEffect}},
            'electric': {'active': False, 'applied': False, 'func': {self.electricEffect}},
            'stunned': {'active': False, 'applied': False, 'func': {self.stunnedEffect}},
            'leeched': {'active': False, 'applied': False, 'func': {self.leechedEffect}},
            'dmg_down': {'active': False, 'applied': False, 'func': {self.dmgDown}},
            'const_down': {'active': False, 'applied': False, 'func': {self.constDown}},
            'charisma_down': {'active': False, 'applied': False, 'func': {self.charismaDown}},
            'intelligence_down': {'active': False, 'applied': False, 'func': {self.intelligenceDown}},
        }
        
    def onFireEffect(self, how_long, amount):
        pass

    def electricEffect(self, how_long, amount):
        pass
    
    def stunnedEffect(self, how_long, amount):
        self.effects['stunned']['applied'] = True
        if not how_long == 0: 
            if 
        else:
            self.effects['stunned']['active'] = False 
    
    def leechedEffect(self, how_long, amount):
        pass
    
    def dmgDown(self, how_long, amount):
        if not how_long == 0:
            self.effects['dmg_down']['applied'] = True
            if not self.effects['dmg_down']['applied']:
                self.target.self_class_damage -= amount
                self.effects['dmg_down']['applied'] = True
            else:
                self.target.self_class_damage += amount 
        else:
            self.effects['dmg_down']['applied'] = False

                

    def constDown(self, how_long, amount):
        pass
    
    def charismaDown(self, how_long, amount):
        pass

    def intelligenceDown(self, how_long, amount):
        pass
