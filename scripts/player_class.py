import pygame as pg

class Player():
    def __init__(self,constitution, health,damage,speed, playerClass, effectOnSelf):
        self.constitution = constitution
        self.health = health
        self.damage = damage
        self.speed = speed

        self.maxHealth = constitution * 4

        self.isDamagingSomeone = False
        
        self.playerClass = playerClass
        
        self.effectOnSelf = effectOnSelf