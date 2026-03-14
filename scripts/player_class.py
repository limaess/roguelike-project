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
