import pygame as pg

class Enemy:
    def __init__(self,constitution, health,speed, strength,dexterity,magic, self_class, self_class_damage, class_weaknesses, howWeak):
        self.constitution = constitution

        self.health = health
        self.speed = speed

        self.strength = strength
        self.dexterity = dexterity
        self.magic = magic

        self.maxHealth = constitution * 4

        self.self_class = self_class

        self.self_class_damage = self_class_damage
        self.class_weaknesses = class_weaknesses
        self.howWeak = howWeak

        self.has_attacked = False

    def basicAttack(self, target): 
        if not self.has_attacked:
            if not self.class_weaknesses == target.self_class:
                target.health -= self.self_class_damage
            else:
                target.health -= (self.your_class_damage - self.how_weak)

        self.has_attacked = True