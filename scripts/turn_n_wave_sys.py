from enemy_class import *
from player_class import *

from player_inventory import *
from items import *


class TurnSys:
    def __init__(self, whos_turn, which_round, exhaustion):
        self.whos_turn = whos_turn
        self.which_round = which_round
        self.exhaustion = exhaustion

        self.turn_thing = None

        self.turn_order = []

        self.ended_round = False
        self.ended_turn = False

    def makeTurnOrder(self,player, enemy1,enemy2,enemy3):
        if not self.turn_order:
            self.turn_order = [player,enemy1,enemy2,enemy3,player]
            return True
        else:
            print('why am i calling this function?')

        self.turn_thing = self.turn_order[self.whos_turn]

    def endRound(self):
        if self.whos_turn == 4: 
            if not self.ended_round:
                self.which_round += 1 
                for these_guys in self.turn_order: # for everyone in the turn_order list thats been sorted before that
                    these_guys.has_attacked = False # they can attack once more when its their turn
                    for item in these_guys.consumable_inventory.extend(these_guys.spell_inventory): # for everything in their consum inv and spell inv 
                        item.been_used = False # they can use it once more when its their turn

    def endTurn(self,caller, caller_inv):
        if not self.ended_turn:
            self.whos_turn += 1

            caller.has_attacked = False

            for item in caller_inv:
                item.been_used = False

            self.ended_turn = True

turnHandler = TurnSys(0, 0, False)