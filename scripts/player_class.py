import pygame as pg

class Player():
    def __init__(self,constitution, health,speed,mana, strength,dexterity,magic, intelligence,charisma, lifesteal, self_class, self_class_damage, effect_on_self, which_spell_used):
        self.constitution = constitution
        self.health = health
        self.speed = speed
        self.mana = mana

        self.strength = strength
        self.dexterity = dexterity
        self.magic = magic

        self.intelligence = intelligence
        self.charisma = charisma

        self.lifesteal = lifesteal

        self.maxHealth = constitution * 4

        self.has_attacked = False
        self.whichSpellUsed = which_spell_used
        
        self.self_class = self_class
        self.self_class_damage = self_class_damage
        self.effect_on_self = effect_on_self

    def basicAttack(self, target):
        if not self.has_attacked:
            if not target.class_weaknesses == self.self_class: 
                target.health -= (self.damage - target.wave_buffs)
            else:
                target.health -= (self.damage + target.howWeak)
        else:
            print('you already attacked, but this message wont appear later')
        self.has_attacked = True

    def limits(self):
        if self.health >= self.max_health:
            self.health = self.max_health
        if self.health <= 0:
            self.health = 0

        if self.mana >= self.charisma:
            self.mana = self.charisma
        if self.mana <= 0:
            self.mana = 0
