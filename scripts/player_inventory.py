import pygame as pg

consumable_inventory = []
spell_inventory = []
passive_inventory = []

all_consumables = []
all_spells = []
all_passives = []

class Consumable:
    def __init__(self, description,name,amount,value, item_func,self_class, uses_left): # amount - for using|value - for selling or whatever
        self.name = name
        self.description = description

        self.amount = amount

        self.value = value

        self.item_func = item_func
        self.uses_left = uses_left

        self.self_class = self_class

        self.been_used = False

    def applyEffect(self, player, target, item, amount):
        if self.uses_left > 0 and not self.been_used:
            self.item_func(player, target, amount, item)
            self.uses_left -= 1
            self.been_used = True

class Passive:
    def __init__(self, description,name,amount,item_func):
        self.name = name
        self.description = description

        self.amount = amount

        self.item_func = item_func

        self.been_used = False  

    def applyEffect(self, player, target, item, amount):
        if self.uses_left > 0 and not self.been_used:
            self.item_func(player, target, amount, item)
            self.been_used = True

class Spell:
    def __init__(self, description,name,  mana_cost,amount, item_func, self_class):
        self.name = name
        self.description = description

        self.amount = amount

        self.item_func = item_func

        self.been_used = False

    def applyEffect(self, player, target, item, amount):
        if self.uses_left > 0 and not self.been_used:
            player.mana -= self.mana_cost
            self.item_func(player, target, amount, item)
            self.been_used = True

class Inventory:
    def __init__(self, max_amt,amt_inside, current_amt_inside, inventory, inventory_value):
        self.max_amt = max_amt
        self.amt_inside = amt_inside
        self.current_amt_inside = current_amt_inside

        self.inventory = inventory

        self.inventory_value = inventory_value
        self.value_calculated = False

    def addItem(self, item):
        if not self.amt_inside >= self.max_amt:
            self.inventory.append(item)
        else:
            print('no')

    def deleteItem(self, item):
        deleted = False
        if item in self.inventory and not deleted:
            self.inventory.remove(item)
            deleted = True
        return deleted

    def deleteOnZeroUses(self, item):
        if item.uses_left == 0 and item in self.inventory:
            self.inventory.remove(item)

    def calculateInvValue(self, item):
        if self.inventory and not self.value_calculated and item in all_consumables: # if there is anything in inventory and value wasnt calculated:
            for x in self.inventory:
                x.value += self.inventory_value # item value adds up to inventory value for every item in inv
                self.current_amt_inside += 1
                self.amt_inside = self.current_amt_inside # genuinely dont know why this is here
            self.value_calculated = True

            if self.amt_inside < self.current_amt_inside or self.amt_inside > self.current_amt_inside: # if amt inside changes in any way
                self.inventory_value = 0 # it does this
                self.value_calculated = False

consum_inv = Inventory(6, 0,0, consumable_inventory, 0)
spell_inv = Inventory(5, 0,0, spell_inventory, 0)
passive_inv = Inventory(10, 0,0, passive_inventory, 0)
