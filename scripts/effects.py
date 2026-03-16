import random as r

from enemy_class import *
from player_class import *

from player_inventory import *

from turn_n_wave_sys import *

class Effect:
    def __init__(self, effects_on_self: list, target, caller, target_consum_inv, target_spell_inv):
        self.target = target
        self.caller = caller

        self.target_consum_inv = target_consum_inv
        self.target_spell_inv = target_spell_inv

        self.effects_on_self = effects_on_self

        self.effects = {
            'on_fire': {'active': False, 'applied': False, 'how_long': 0, 'func': {self.onFireEffect}},
            'electric': {'active': False, 'applied': False, 'how_long': 0, 'func': {self.electricEffect}},
            'stunned': {'active': False, 'applied': False, 'how_long': 0, 'func': {self.stunnedEffect}},
            'leeched': {'active': False, 'applied': False, 'how_long': 0, 'func': {self.leechedEffect}},
            'dmg_down': {'active': False, 'applied': False, 'how_long': 0, 'func': {self.dmgDown}},
            'const_down': {'active': False, 'applied': False, 'how_long': 0, 'func': {self.constDown}},
            'charisma_down': {'active': False, 'applied': False, 'how_long': 0, 'func': {self.charismaDown}},
            'intelligence_down': {'active': False, 'applied': False, 'how_long': 0, 'func': {self.intelligenceDown}},
        }
        
    def onFireEffect(self, amount):
        self.effects['on_fire']['active'] = True
        if not self.effects['on_fire']['how_long'] == 0 and not self.effects['on_fire']['applied']: 
            self.target.health -= amount 
            amount += 5
            self.effects['on_fire']['applied'] = True

    def electricEffect(self, amount):
        self.effects['electric']['active'] = True
        if not self.effects['electric']['how_long'] == 0 and not self.effects['electric']['applied']: 
            self.target.health -= amount 
            self.effects['electric']['applied'] = True
        else:
            self.effects['electric']['active'] = False

    def stunnedEffect(self, amount):
        self.effects['stunned']['active'] = True
        if not self.effects['stunned']['how_long'] == 0:
            if turnHandler.turn_order[turnHandler.whos_turn] == self.target:
                turnHandler.whos_turn += 1
        else:
            self.effects['stunned']['active'] = False 
    
    def leechedEffect(self,amount):
        self.effects['leeched']['active'] = True
        if not self.effects['leeched']['how_long'] == 0 and not self.effects['leeched']['applied']:
            self.target.health -= amount
            self.caller.health += amount
            self.effects['leeched']['applied'] = True
        else:
            self.effects['leeched']['active'] = False 
    
    def dmgDown(self,amount):
        if not self.effects['dmg_down']['how_long'] == 0:
            self.effects['dmg_down']['active'] = True
            if not self.effects['dmg_down']['applied']:
                self.target.self_class_damage -= amount
                self.effects['dmg_down']['applied'] = True
            else:
                self.target.self_class_damage += amount 
        else:
            self.effects['dmg_down']['active'] = False

                

    def constDown(self, how_long, amount):
        if not self.effects['const_down']['how_long'] == 0:
            self.effects['const_down']['active'] = True
            if not self.effects['const_down']['applied']:
                self.target.constitution -= amount
                self.effects['const_down']['applied'] = True
            else:
                self.target.constitution += amount   
        else:
            self.effects['const_down']['active'] = False

    
    def charismaDown(self, how_long, amount):
        if not self.effects['charisma_down']['how_long'] == 0:
            self.effects['charisma_down']['active'] = True
            if not self.effects['charisma_down']['applied']:
                self.target.charisma -= amount
                self.effects['charisma_down']['applied'] = True
            else:
                self.target.charisma += amount   
        else:
            self.effects['charisma_down']['active'] = False

    def intelligenceDown(self, how_long, amount):
        pass
