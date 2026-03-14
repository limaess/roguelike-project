import pygame as pg

inventory = []

class Consumables:
    def __init__(self, description,name,amount,value, item_func, uses_left): # amount - for using|value - for selling or whatever
        self.name = name
        self.description = description

        self.amount = amount

        self.value = value

        self.item_func = item_func
        self.uses_left = uses_left

class Inventory:
    def __init__(self, max_amt,amt_inside, current_amt_inside, inventory_value):
        self.max_amt = max_amt
        self.amt_inside = amt_inside
        self.current_amt_inside = current_amt_inside

        self.inventory_value = inventory_value
        self.value_calculated = False

    def addItem(self, item):
        if not self.amt_inside >= self.max_amt:
            inventory.append(item)
        else:
            print('no')
    def deleteItem(self, item):
        inventory.remove(item)

    def calculateInvValue(self):
        if inventory and not self.value_calculated: # if there is anything in inventory and value wasnt calculated:
            for item in inventory:
                item.value += self.inventory_value # item value adds up to inventory value for every item in inv
                self.current_amt_inside += 1
                self.amt_inside = self.current_amt_inside # genuinely dont know why this is here
            self.value_calculated = True

            if self.amt_inside < self.current_amt_inside or self.amt_inside > self.current_amt_inside: # if amt inside changes in any way
                self.inventory_value = 0 # it does this
                self.value_calculated = False

class_inventory = Inventory(max_amt=6,amt_inside=0,current_amt_inside=0,inventory_value=0)