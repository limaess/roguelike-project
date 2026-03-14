import pygame as pg

class Enemy:
    def __init__(self,constitution, health,speed, strength,dexterity,magic, classWeaknesses, howWeak):
        self.constitution = constitution

        self.health = health
        self.speed = speed

        self.strength = strength
        self.dexterity = dexterity
        self.magic = magic

        self.maxHealth = constitution * 4

        self.classWeaknesses = classWeaknesses
        self.howWeak = howWeak
