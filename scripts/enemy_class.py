import pygame as pg

class Enemy:
    def __init__(self,constitution, health,speed, strength,dexterity,magic, selfClassDamage, classWeaknesses, howWeak):
        self.constitution = constitution

        self.health = health
        self.speed = speed

        self.strength = strength
        self.dexterity = dexterity
        self.magic = magic

        self.maxHealth = constitution * 4

        self.selfClassDamage = selfClassDamage
        self.classWeaknesses = classWeaknesses
        self.howWeak = howWeak

    def basicAttack(self, target): 
        if not self.hasAttacked:
            if not self.classWeaknesses == target.playerClass:
                target.health -= self.yourClassDamage 
            else:
                target.health -= (self.yourClassDamage - self.howWeak)

        self.hasAttacked = True
