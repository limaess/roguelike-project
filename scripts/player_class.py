import pygame as pg

class Player():
    def __init__(self,constitution, health,speed,mana, strength,dexterity,magic, intelligence,charisma, lifesteal, playerClass, yourClassDamage, effectOnSelf, whichSpellUsed):
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

        self.hasAttacked = False
        self.whichSpellUsed = whichSpellUsed
        
        self.playerClass = playerClass
        self.yourClassDamage = yourClassDamage
        self.effectOnSelf = effectOnSelf

    def basicAttack(self, target):
        if not self.hasAttacked:
            if not target.classWeaknesses == self.playerClass: 
                target.health -= (self.damage - target.waveBuffs)
            else:
                target.health -= (self.damage + target.howWeak)
        else:
            print('you already attacked, but this message wont appear later')
        self.hasAttacked = True

    def limits(self):
        if self.health >= self.maxHealth:
            self.health = self.maxHealth
        if self.health <= 0:
            self.health = 0

        if self.mana >= self.charisma:
            self.mana = self.charisma
        if self.mana <= 0:
            self.mana = 0
