import pygame as pg

#------------------------------------- consumables
#-------------------------- potion-type consum

def healEffect(player, target, amount, item):
    if not item.beenUsed:
            target.health += amount

def attackPotionEffect(player, target, amount, item):
    if not item.beenUsed:
            target.damage += amount

#-------------------------- melee




#-------------------------- dexterity




#-------------------------- magic




#------------------------------------- passives




#------------------------------------- spells  
#-------------------------- melee




#-------------------------- dexterity




#-------------------------- magic




#-------------------------- other spells 
#------------------------------------- passive effects