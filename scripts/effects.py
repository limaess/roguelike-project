import random as r
import pygame as pg

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
            'on_fire': {'active': False, 'applied': False, 'amount': 0, 'how_long': 0, 'func': self.onFireEffect},
            'electric': {'active': False, 'applied': False, 'amount': 0, 'how_long': 0, 'func': self.electricEffect},
            'stunned': {'active': False, 'applied': False,'amount': 0,  'how_long': 0, 'func': self.stunnedEffect},
            'leeched': {'active': False, 'applied': False,'amount': 0,  'how_long': 0, 'func': self.leechedEffect},
            'dmg_down': {'active': False, 'applied': False,'amount': 0,  'how_long': 0, 'func': self.dmgDown},
            'const_down': {'active': False, 'applied': False,'amount': 0,  'how_long': 0, 'func': self.constDown},
            'charisma_down': {'active': False, 'applied': False,'amount': 0,  'how_long': 0, 'func': self.charismaDown},
            'intelligence_down': {'active': False, 'applied': False,'amount': 0,  'how_long': 0, 'func': self.intelligenceDown},
        }

    def applyEffect(self,effect, how_long, amount, target, caller):
        self.target = target
        self.caller = caller

        self.effects[effect]['how_long'] = how_long
        self.effects[effect]['amount'] = amount  

        self.effects[effect]['func']()
        self.effects_on_self.append(effect)
        
    def onFireEffect(self):
        self.effects['on_fire']['active'] = True
        if not self.effects['on_fire']['how_long'] == 0 and not self.effects['on_fire']['applied']: 
            self.target.health -= self.effects['on_fire']['amount']  
            self.effects['on_fire']['amount'] += 5
            self.effects['on_fire']['how_long'] -= 1
            self.effects['on_fire']['applied'] = True
        if self.effects['on_fire']['how_long'] == 0:
            self.effects['on_fire']['active'] = False

        if turnHandler.turn_order[turnHandler.whos_turn] == self.target:
            self.effects['on_fire']['applied'] = False

    def electricEffect(self):
        self.effects['electric']['active'] = True
        if not self.effects['electric']['how_long'] == 0 and not self.effects['electric']['applied']: 
            self.target.health -= self.effects['electric']['amount']  
            self.effects['electric']['how_long'] -= 1
            self.effects['electric']['applied'] = True
        else:
            self.effects['electric']['active'] = False

        if turnHandler.turn_order[turnHandler.whos_turn] == self.target:
            self.effects['electric']['applied'] = False

    def stunnedEffect(self):
        self.effects['stunned']['active'] = True
        if not self.effects['stunned']['how_long'] == 0:
            if turnHandler.turn_order[turnHandler.whos_turn] == self.target:
                turnHandler.whos_turn += 1
        else:
            self.effects['stunned']['active'] = False 
    
    def leechedEffect(self):
        self.effects['leeched']['active'] = True
        if not self.effects['leeched']['how_long'] == 0 and not self.effects['leeched']['applied']:
            self.target.health -= self.effects['leeched']['amount']  
            self.caller.health += self.effects['leeched']['amount']  
            self.effects['leeched']['how_long'] -= 1
            self.effects['leeched']['applied'] = True
        else:
            self.effects['leeched']['active'] = False 

        if turnHandler.turn_order[turnHandler.whos_turn] == self.target:
            self.effects['leeched']['applied'] = False
    
    def dmgDown(self):
        if not self.effects['dmg_down']['how_long'] == 0:
            self.effects['dmg_down']['active'] = True
            if not self.effects['dmg_down']['applied']:
                self.target.self_class_damage -= self.effects['dmg_down']['amount']  
                self.effects['dmg_down']['applied'] = True
            else:
                self.target.self_class_damage += self.effects['dmg_down']['amount']  
        else:
            self.effects['dmg_down']['active'] = False


    def constDown(self):
        if not self.effects['const_down']['how_long'] == 0:
            self.effects['const_down']['active'] = True
            if not self.effects['const_down']['applied']:
                self.target.constitution -= self.effects['const_down']['amount']  
                self.effects['const_down']['applied'] = True
            else:
                self.target.constitution += self.effects['const_down']['amount']  
        else:
            self.effects['const_down']['active'] = False

    
    def charismaDown(self):
        if not self.effects['charisma_down']['how_long'] == 0:
            self.effects['charisma_down']['active'] = True
            if not self.effects['charisma_down']['applied']:
                self.target.charisma -= self.effects['charisma_down']['amount']  
                self.effects['charisma_down']['applied'] = True
            else:
                self.target.charisma += self.effects['charisma_down']['amount']  
        else:
            self.effects['charisma_down']['active'] = False

    def intelligenceDown(self):
        if not self.effects['intelligence_down']['how_long'] == 0:
            self.effects['intelligence_down']['active'] = True
            if not self.effects['intelligence_down']['applied']:
                self.target.intelligence -= self.effects['intelligence_down']['amount']  
                self.effects['intelligence_down']['applied'] = True
            else:
                self.target.intelligence += self.effects['intelligence_down']['amount']    
        else:
            self.effects['intelligence_down']['active'] = False

pg.init()

player = Player(25, 100, 10, 30, 10, 20, 5, 4, 30, 0, 'ranger', None, None, None)
player.self_class_damage = player.dexterity

turnHandler.makeTurnOrder(player, 'place', 'holder', 'lmao')    
turnHandler.whos_turn = 0

playerEffects = Effect([], None, None, None, None)
playerEffects.applyEffect('on_fire', how_long=10, amount=5, target=player, caller=None)

screen = pg.display.set_mode((800, 600))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.display.flip()

    keys = pg.key.get_just_pressed()

    if keys[pg.K_q]:
        turnHandler.whos_turn += 1
        print(player.health, print(turnHandler.whos_turn)) 

        for effect in playerEffects.effects_on_self:
            playerEffects.effects[effect]['func']()

        if turnHandler.whos_turn == 2:
            print('PLAYER DETECTED!!!!')    
            if playerEffects.effects[effect]['how_long'] == 0:
                print('BOOOO YOU SUCK')

    if turnHandler.whos_turn >= 4:
        turnHandler.whos_turn = -1