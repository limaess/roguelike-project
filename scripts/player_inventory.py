import pygame as pg

inventory = []
class Inventory():
    def __init__(self, max_amt,amt_inside, current_amt_inside, inventory_value):
        self.max_amt = max_amt
        self.amt_inside = amt_inside
        self.current_amt_inside = current_amt_inside

        self.inventory_value = inventory_value
        self.value_calculated = False

    def calculateInvValue(self):
        if inventory and not self.value_calculated: 
            for item in inventory:
                item.value += self.inventory_value
                self.current_amt_inside += 1
                self.amt_inside = self.current_amt_inside
            self.value_calculated = True

            if self.amt_inside < self.current_amt_inside or self.amt_inside > self.current_amt_inside:
                self.inventory_value = 0
                self.value_calculated = False

class_inventory = Inventory(max_amt=6,amt_inside=0,current_amt_inside=0,inventory_value=0)