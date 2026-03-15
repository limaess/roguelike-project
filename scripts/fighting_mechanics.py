import pygame as pg

class TurnSys:
    def __init__(self, whos_turn, which_round, exhaustion):
        self.whos_turn = whos_turn
        self.which_round = which_round
        self.exhaustion = exhaustion

        self.turn_thing = None

        self.turn_order = []

    def makeTurnOrder(self,player, enemy1,enemy2,enemy3):
        if not self.turn_order:
            self.turn_order = [player,enemy1,enemy2,enemy3,player]
        else:
            print('why am i calling this function?')

        self.turn_thing = self.turn_order[self.whos_turn]